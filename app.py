import random
import time
import socket

from flask import Flask, request, render_template, session, redirect
from flask_socketio import SocketIO, join_room, leave_room, emit, send
import json

import game


# ----- SET LOCAL OR DROPLET IP ADDRESS ----- #
def set_ip():
    """
    If the application runs on the droplet it returns with the droplet's IP
    Otherwise it returns with '127.0.0.1' string.
    :return: str = droplet's IP or localhost
    """

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(("8.8.8.8", 80))  # Connect to Google's DNS server
        local_ip_address = s.getsockname()[0]  # Get the local IP address

    if local_ip_address == '134.122.79.248':
        return local_ip_address
    else:
        return '127.0.0.1'


IP_ADDRESS = set_ip()
# ----- SET LOCAL OR DROPLET IP ADDRESS ----- #

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret'
app.config['SESSION_TYPE'] = 'filesystem'

socketio = SocketIO(app, manage_session=False)

player_points = dict()  # {lobby:{player1:0,player2:0}}

game_objects = dict()


@app.route('/tabla', methods=['POST'])
def tabla():
    session.clear()
    if request.method == 'POST':
        print(request.get_data())

        host_image = request.form.get('hostPicId')
        opponent_image = request.form.get('opponentPicId')

        player_side = request.form.get('side')
        lobby_id = request.form.get('lobbyID')
        lobby_name = request.form.get('lobbyName')
        player1_id = request.form.get('player1ID')
        player1_name = request.form.get('player1Name')
        player2_id = request.form.get('player2ID')
        player2_name = request.form.get('player2Name')
        host_name = request.form.get('hostPlayerName')
        opponent_name = request.form.get('opponentPlayerName')

        if lobby_id not in game_objects:
            game_object = game.Game(lobby_id,
                                    lobby_name,
                                    player1_id,
                                    player1_name,
                                    player2_id,
                                    player2_name,
                                    host_name,
                                    opponent_name,
                                    player_side,
                                    host_image,
                                    opponent_image
                                    )
            game_object.refresh_status()
            game_objects[game_object.get_lobby_id()] = game_object
        else:
            game_object = game_objects[lobby_id]
            game_object.refresh_status()

        while not game_object.get_status():
            time.sleep(0.1)

        session['lobby_name'] = game_object.get_lobby_name()
        session['lobby_id'] = game_object.get_lobby_id()
        session['host_name'] = game_object.get_host_name()
        session['host_name_id'] = game_object.get_host_id()
        session['host_point'] = game_object.get_host_point()
        session['opponent_name'] = game_object.get_opponent_name()
        session['opponent_name_id'] = game_object.get_opponent_id()
        session['opponent_point'] = game_object.get_opponent_point()
        session['player1_name'] = player1_name
        session['player1_id'] = game_object.get_player_id(player1_name)
        session['player2_name'] = player2_name
        session['player2_id'] = game_object.get_player_id(player2_name)
        session['player1_pt'] = game_object.get_point(player1_name)
        session['player2_pt'] = game_object.get_point(player2_name)
        session['host_color'] = game_object.get_color(game_object.get_host_name())
        session['opponent_color'] = game_object.get_color(game_object.get_opponent_name())
        session['host_side'] = game_object.get_host_side()
        session['opponent_side'] = game_object.get_opponent_side()
        session['player_side'] = game_object.get_side(player1_name)
        session['host_imege'] = game_object.get_host_image()
        session['opponent_image'] = game_object.get_opponent_image()

        return render_template('table.html', session=session)
    else:
        redirect(set_ip() + ':5050')


@socketio.on("connect")
def connect():
    room = session.get('lobby_id')
    player1 = session.get('player1_name')
    player2 = session.get('player2_name')
    join_room(room)
    print(f"{player1} is in room {room}")


@socketio.on("disconnect")
def disconnect():
    lobby = session.get('lobby_id')
    player = session.get('player1_name')
    global game_objects
    game_object = game_objects[lobby]
    game_object.set_player_disconnect(player)

    leave_room(lobby)
    print(f"{lobby} leave room {lobby}")


@socketio.on("start_game")
def start_game(data):
    print("START GAME", data)
    lobby = data['lobby_id']
    player = data['player']
    status = data['status']
    global game_objects
    game_object = game_objects[lobby]
    game_object.set_player_connect(player)
    while not game_object.is_players_connect():
        time.sleep(0.1)

    if player == game_object.get_host_name():
        data = {'data_type': 'start_game',
                'status': True}
        send(data, to=lobby, json=True)


@socketio.on("get_question_event")
def get_question_event(data):
    lobby = data['lobby_id']
    player = data['player']
    question_type = data['question_type']
    global game_objects
    game_object = game_objects[lobby]

    if player == game_object.get_host_name():
        lobby_question = game_object.get_question()

        if str(question_type) == "1":
            lobby_question = game_object.get_question()
        else:
            lobby_question = game_object.get_question("2")

        data_html = render_template(f'question_type_{question_type}.html', lobby_question=lobby_question)
        print('Question sent to lobby')
        data = {'data_type': 'question', 'question_type': question_type, 'data_html': data_html,
                'lobby_question': lobby_question}
        send(data, to=lobby, json=True)


@socketio.on("get_score")
def get_score_event(data):
    lobby = data['lobby_id']
    player = data['player']
    global game_objects
    game_object = game_objects[lobby]

    data['data_type'] = 'get_score'
    send(data, to=lobby, json=True)


@socketio.on("surr")
def surr(data):
    data["data_type"] = 'surrender'
    lobby = data['lobby']
    player = data['player']
    global game_objects
    game_object = game_objects[lobby]
    game_object.set_point_null(player)
    data["host_point"] = game_object.get_host_point()
    data["opponent_point"] = game_object.get_opponent_point()
    send(data, to=lobby, json=True)


@socketio.on("answers")
def get_answers(data):
    time.sleep(3)
    global game_objects
    print("ANSWERSBOL")
    if data['question_type'] == 1:
        lobby = data['lobby_id']
        player = data['player']
        answer = data['answer']

        game_object = game_objects[lobby]

        game_object.set_last_answer(player, answer)
        if answer:
            game_object.set_point(player)
            data = {
                'data_type': "point_refresh",
                'host_point': game_object.get_host_point(),
                'opponent_point': game_object.get_opponent_point()
            }
            send(data, to=lobby, json=True)

        while not game_object.has_answers():
            time.sleep(0.1)
        """Ha mind a 2 valasz rosz"""
        if player == game_object.get_host_name():
            if game_object.get_last_answer_host() == False and game_object.get_last_answer_opponent() == False:
                print("Mind a 2 valasz rosz")
                game_object.del_last_answer_all()
                """Kerunk uj kerdest"""
                data = {
                    "lobby_id": lobby,
                    'question_type': 1,
                    "player": player

                }
                get_question_event(data)

            elif game_object.get_last_answer_host() == True and game_object.get_last_answer_opponent() == True:
                print("Mind a 2 valasz jo")
                game_object.del_last_answer_all()

                data = {
                    "lobby_id": lobby,
                    "data_type": "host_and_opponent_select_area",
                    "player": game_object.get_host_name()
                }
                send(data, to=lobby, json=True)


            elif game_object.get_last_answer_host() == True and game_object.get_last_answer_opponent() == False:
                print("Host jo, opponent rosz")
                game_object.del_last_answer_all()
                """
                HOST VALASZT CELLAT 
                kuldunk egy ertesitest 
                host nak is meg opponentnek
                ahol a host valaszt
                opponent meg kusol
                aztan a valasztas utan 
                kerunk uj kerdest
                """
                data = {
                    "lobby_id": lobby,
                    "data_type": "opponent_select_area",
                    "player": game_object.get_host_name()
                }
                send(data, to=lobby, json=True)

            elif game_object.get_last_answer_host() == False and game_object.get_last_answer_opponent() == True:
                print("Host rosz, opponent jo")
                game_object.del_last_answer_all()
                data = {
                    "lobby_id": lobby,
                    "data_type": "host_select_area",
                    "player": game_object.get_opponent_name()
                }
                send(data, to=lobby, json=True)
    elif data['question_type'] == 2:
        player = data['player']
        lobby = data['lobby_id']
        answer = data['answer']
        ans_time = data['ans_time']
        distance = data['distance']

        game_object = game_objects[lobby]

        game_object.set_last_answer_time(player, ans_time, answer)
        game_object.set_last_answer_distance(player, distance)

        print(f"get_faster_better_last {game_object.has_last_answers_time()}")
        while not game_object.has_last_answers_time():
            print(f"wait --- {player}")
            time.sleep(1)

        # game_object.del_last_answer_all()
        # game_object.del_last_answer_distance_all()
        # game_object.del_last_anser_time_all()

        if player == game_object.get_host_name():
            better = game_object.get_faster_better_last()
            game_object.set_point(better, point_number=250)
            print(f"""{better},{game_object.get_host_name()},{game_object.get_opponent_name()}
            "player": {game_object.get_host_name()},
                    'host_point': {game_object.get_host_point()},
                    'opponent_point': {game_object.get_opponent_point()}
            """)
            print("host tovabbit")
            if better == game_object.get_host_name():
                print("host a jobb")
                data = {
                    "lobby_id": lobby,
                    "data_type": "opponent_select_area_and_point_refresh",
                    "player": game_object.get_host_name(),
                    'host_point': game_object.get_host_point(),
                    'opponent_point': game_object.get_opponent_point()
                }
                send(data, to=lobby, json=True)
            else:
                print("oppoent a jobb")
                data = {
                    "lobby_id": lobby,
                    "data_type": "host_select_area_and_point_refresh",
                    "player": game_object.get_opponent_name(),
                    'host_point': game_object.get_host_point(),
                    'opponent_point': game_object.get_opponent_point()
                }
                send(data, to=lobby, json=True)


@socketio.on("point_event")
def point_event(data):
    lobby_id = data['lobby_id']
    lobby_name = data['lobby_name']
    player_name = data['player_name']
    question_id = data['question_id']
    answer = data['answer']
    global game_objects
    game_object = game_objects[lobby_id]
    if answer:  # ha jo a valasz akkor kap pontot
        game_object.set_point(player_name)

    game_object.set_last_point(player_name, answer)
    while not game_object.has_points():
        time.sleep(0.1)

    game_object.del_last_point_all()

    data = {
        'data_type': "point_refresh",
        'host_point': game_object.get_host_point(),
        'opponent_point': game_object.get_opponent_point()
    }
    send(data, to=lobby_id, json=True)


@socketio.on("start_selecting_area")
def area_select_event(data):
    """EZT A FUGVENYT CSAK A HOST HIVJA"""
    lobby_id = data['lobby_id']
    lobby_name = data['lobby_name']
    player_name = data['player_name']
    question_id = data['question_id']
    answer = data['answer']

    global game_objects
    game_object = game_objects[lobby_id]
    while not game_object.has_points():
        time.sleep(0.1)
    if game_object.get_host_name() == player_name and answer:
        data = []
        data = {"player_name": player_name,
                'data_type': "host_select_area"}
        send(data, to=lobby_id, json=True)
    elif game_object.get_host_name() == player_name and not answer:
        """Ha az opponent helyesen valaszolt a host meg roszul"""
        if game_object.get_last_point(game_object.get_opponent_name()):
            data = []
            data = {"player_name": game_object.get_opponent_name(),
                    'data_type': "opponent_select_area"}
            send(data, to=lobby_id, json=True)
        else:
            data = {"player_name": game_object.get_opponent_name(),
                    'data_type': "2_incorrect_answer_event"}
            send(data, to=lobby_id, json=True)
    """Itt kell fojtatni, mi tortenik ha rosz a host valasza  """


@socketio.on("collect_area_event")
def collect_area_event(data):
    lobby_id = data['lobby_id']
    button_id = data['button_id']
    player = data["player"]

    global game_objects
    game_object = game_objects[lobby_id]
    data["color"] = game_object.get_color(player)
    """TO OD itt lehet szerver oldalon lementeni a kivalasztot teruleteket"""

    data["data_type"] = 'collect_area_event'

    send(data, to=lobby_id, json=True)


@socketio.on("collect_area_event_for_new_select")
def collect_area_event(data):
    lobby_id = data['lobby_id']
    button_id = data['button_id']
    player = data["player"]

    global game_objects
    game_object = game_objects[lobby_id]
    data["color"] = game_object.get_color(player)
    """TO OD itt lehet szerver oldalon lementeni a kivalasztot teruleteket"""
    data["player"] = game_object.get_opponent_name()
    data["host_player"] = game_object.get_host_name()
    data["data_type"] = 'collect_area_event_for_new_select'

    send(data, to=lobby_id, json=True)


@socketio.on("continue_selecting_area")
def continue_selecting_area(data):
    """EZT CSAK A HOST KULDI"""
    print("continue_selecting_area", data)
    lobby_id = data['lobby_id']
    player_name = data["player"]
    global game_objects
    game_object = game_objects[lobby_id]
    if game_object.get_opponent_name() != player_name:
        print("ELSO IF")
        if game_object.get_last_point(game_object.get_opponent_name()):
            data = {"player_name": game_object.get_opponent_name(),
                    'data_type': "opponent_select_area"}
            game_object.del_last_point_all()
            send(data, to=lobby_id, json=True)
        else:
            game_object.del_last_point_all()
            print('Rosz valasz opponent')


@socketio.on("start_battle")
def start_battle(data):
    print(data)
    lobby_id = data['lobby_id']
    data['data_type'] = "start_battle"
    print(data)
    send(data, to=lobby_id, json=True)


@socketio.on("get_battle_question_event")
def get_battle_question_event(data):
    lobby = data['lobby_id']
    player = data['player']
    question_type = data['question_type']
    global game_objects
    game_object = game_objects[lobby]

    if player == game_object.get_host_name():
        game_object.del_last_answer_all()
        game_object.del_last_answer_distance_all()
        game_object.del_last_anser_time_all()
        lobby_question = game_object.get_question()

        if str(question_type) == "1":
            lobby_question = game_object.get_question()
        else:
            lobby_question = game_object.get_question("2")

        data_html = render_template(f'question_type_{question_type}.html', lobby_question=lobby_question)
        print('Question sent to lobby')
        data = {'data_type': 'battle_question', 'question_type': question_type, 'data_html': data_html,
                'lobby_question': lobby_question}
        send(data, to=lobby, json=True)


@socketio.on("battle_answers")
def battle_answers(data):
    print(data)

    if data['question_type'] == 2:
        player = data['player']
        lobby = data['lobby_id']
        answer = data['answer']
        ans_time = data['ans_time']
        distance = data['distance']

        game_object = game_objects[lobby]

        game_object.set_last_answer_time(player, ans_time, answer)
        game_object.set_last_answer_distance(player, distance)

        print(f"get_faster_better_last {game_object.has_last_answers_time()}")
        while not game_object.has_last_answers_time():
            print(f"wait --- {player}")
            time.sleep(1)

        if player == game_object.get_host_name():
            better = game_object.get_faster_better_last()
            game_object.set_point(better, point_number=250)
            data = {
                "lobby_id": lobby,
                "data_type": "point_refresh_battle",
                "player": game_object.get_host_name(),
                'host_point': game_object.get_host_point(),
                'opponent_point': game_object.get_opponent_point()
            }
            send(data, to=lobby, json=True)


if __name__ == '__main__':
    socketio.run(app, host=IP_ADDRESS, port=5000, allow_unsafe_werkzeug=True)
    # socketio.run(app)
