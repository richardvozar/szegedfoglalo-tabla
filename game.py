from player import Player
from quiz import Quiz
from moduls import revers_side


class Game:
    def __init__(self,
                 lobby_id,
                 lobby_name,
                 player1_id,
                 player1_name,
                 player2_id,
                 player2_name,
                 host_name,
                 opponent_name,
                 player_side,
                 host_image,
                 opponent_image):
        self.lobby_id = lobby_id
        self.lobby_name = lobby_name
        self.status = False
        self.status_pt = 0
        if host_name == player1_name:
            self.host = Player(player1_name, player1_id, 0, '#4A53A7', True, False, player_side,host_image)
            self.opponent = Player(player2_name, player2_id, 0, '#BF2C2C', False, True, revers_side(player_side),opponent_image)
        else:
            self.host = Player(player2_name, player2_id, 0, '#4A53A7', True, False, revers_side(player_side),host_image)
            self.opponent = Player(player1_name, player1_id, 0, '#BF2C2C', False, True, player_side,opponent_image)
        self.quiz = Quiz()
        self.quiz.shuffle_questions()
        self.can_select = []

    def __str__(self):
        return f"""{self.lobby_name} {self.lobby_id}
         """

    def get_host_image(self):
        return self.host.get_image()

    def get_opponent_image(self):
        return self.opponent.get_image()

    def get_faster(self):
        print(f"get faster {self.get_host_last_answer_time()} >= {self.get_opponent_last_answer_time()}")
        if self.get_host_last_answer_time() <= self.get_opponent_last_answer_time():
            print(f"get better{self.get_host_name()}")
            return self.get_host_name()
        else:
            print(f"get better{self.get_opponent_name()}")
            return self.get_opponent_name()

    def get_better(self):
        print(f"get_better {self.host.get_last_answer_distance()} > {abs(self.host.get_last_answer_distance())} ")
        if abs(self.host.get_last_answer_distance()) > abs(self.opponent.get_last_answer_distance()):
            print(f"get better{self.opponent.get_player_name()}")
            return self.opponent.get_player_name()
        else:
            print(f"get better{self.host.get_player_name()}")
            return self.host.get_player_name()

    def get_faster_better_last(self):
        print(f"""
        get_faster_better_last
        ---{self.host.get_last_answer_time()}
        ---{self.host.get_last_answer_time_answer()}
        ---{self.opponent.get_last_answer_time()}
        ---{self.opponent.get_last_answer_time_answer()}
        """)


        if self.host.get_last_answer_time_answer() == True and self.opponent.get_last_answer_time_answer() == True:
            print("mind 2 jo valasz gyorsab : ")
            return self.get_faster()
        elif self.host.get_last_answer_time_answer() == True and self.opponent.get_last_answer_time_answer() == False:
            print("Host jo valasz opponent rosz")
            return self.get_host_name()
        elif self.host.get_last_answer_time_answer() == False and self.opponent.get_last_answer_time_answer() == True:
            print("Opponent jo valasz host rosz")
            return self.get_opponent_name()
        elif self.host.get_last_answer_time_answer() == False and self.opponent.get_last_answer_time_answer() == False:
            print("mind 2 rosz valasz pontosabb : ")
            return self.get_better()
        return "HIBA"

    def del_last_answer_distance_all(self):
        self.host.set_last_answer_distance()  # default 10000
        self.opponent.set_last_answer_distance()

    def set_last_answer_distance(self, player, distance):
        if self.host.get_player_name() == player:
            self.host.set_last_answer_distance(distance)
        elif self.opponent.get_player_name() == player:
            self.opponent.set_last_answer_distance(distance)

    def has_last_answers_time(self):
        if self.host.has_last_answer_time() == True and self.opponent.has_last_answer_time() == True:
            return True
        else:
            return False

    def del_last_anser_time_all(self):
        self.host.set_last_answer_time("","")
        self.opponent.set_last_answer_time("","")

    def get_host_last_answer_time(self):
        return self.host.get_last_answer_time()

    def get_opponent_last_answer_time(self):
        return self.opponent.get_last_answer_time()

    def set_last_answer_time(self, player, time,answer):
        if self.host.get_player_name() == player:
            self.host.set_last_answer_time(time,answer)
        elif self.opponent.get_player_name() == player:
            self.opponent.set_last_answer_time(time,answer)

    def get_side(self, player):
        if self.host.get_player_name() == player:
            return self.host.get_side()
        elif self.opponent.get_player_name() == player:
            return self.opponent.get_side()

    def get_host_side(self):
        return self.host.get_side()

    def get_opponent_side(self):
        return self.opponent.get_side()

    def clear_can_select(self):
        self.can_select = []

    def add_can_select(self, player):
        self.can_select.append(player)

    def get_can_select(self):
        return self.can_select

    def wait(self):
        self.quiz.wait()

    def refresh_status(self):
        self.status_pt += 1
        if self.status_pt == 2:
            self.status = True

    def is_players_connect(self):
        if self.host.is_connected() == True and self.opponent.is_connected() == True:
            return True
        else:
            return False

    def is_player_connect(self, player):
        if self.host.get_player_name() == player:
            return self.host.is_connected()
        elif self.opponent.get_player_name() == player:
            return self.opponent.is_connected()

    def set_player_connect(self, player):
        if self.host.get_player_name() == player:
            self.host.set_connect()
        elif self.opponent.get_player_name() == player:
            self.opponent.set_connect()

    def set_player_disconnect(self, player):
        if self.host.get_player_name() == player:
            self.host.set_disconnect()
        elif self.opponent.get_player_name() == player:
            self.opponent.set_disconnect()

    def set_point(self, player, point_number=100):
        print(f"setpointbol{player}")
        if self.host.get_player_name() == player:
            self.host.set_player_point(point_number)
        elif self.opponent.get_player_name() == player:
            self.opponent.set_player_point(point_number)

    def set_point_null(self, player):
        if self.host.get_player_name() == player:
            self.host.reset_point()
        elif self.opponent.get_player_name() == player:
            self.opponent.reset_point()

    def set_last_point(self, player, point):
        if self.host.get_player_name() == player:
            self.host.add_last_point(point)
        elif self.opponent.get_player_name() == player:
            self.opponent.add_last_point(point)

    def has_points(self):
        if self.host.has_last_point() == True and self.opponent.has_last_point() == True:
            return True
        else:
            return False

    def del_last_point(self, player):
        if self.host.get_player_name() == player:
            self.host.del_last_point()
        elif self.opponent.get_player_name() == player:
            self.opponent.del_last_point()

    def del_last_point_all(self):
        self.host.del_last_point()
        self.opponent.del_last_point()

    def get_last_point(self, player):
        if self.host.get_player_name() == player:
            return self.host.get_last_point()
        elif self.opponent.get_player_name() == player:
            return self.opponent.get_last_point()

    def set_last_answer(self, player, answer):
        if self.host.get_player_name() == player:
            self.host.add_last_answer(answer)
        elif self.opponent.get_player_name() == player:
            self.opponent.add_last_answer(answer)

    def has_answers(self):
        if self.host.has_last_answer() == True and self.opponent.has_last_answer() == True:
            return True
        else:
            return False

    def del_last_answer(self, player):
        if self.host.get_player_name() == player:
            self.host.del_last_answer()
        elif self.opponent.get_player_name() == player:
            self.opponent.del_last_answer()

    def del_last_answer_all(self):
        self.host.del_last_answer()
        self.opponent.del_last_answer()

    def get_last_answer(self, player):
        if self.host.get_player_name() == player:
            return self.host.get_last_answer()
        elif self.opponent.get_player_name() == player:
            return self.opponent.get_last_answer()

    def get_last_answer_host(self):
        return self.host.get_last_answer()

    def get_last_answer_opponent(self):
        return self.opponent.get_last_answer()

    def get_point(self, player):
        if self.host.get_player_name() == player:
            return self.host.get_player_point()
        elif self.opponent.get_player_name() == player:
            return self.opponent.get_player_point()

    def get_host_point(self):
        return self.host.get_player_point()

    def get_opponent_point(self):
        return self.opponent.get_player_point()

    def get_player_id(self, player):
        if self.host.get_player_name() == player:
            return self.host.get_player_id()
        elif self.opponent.get_player_name() == player:
            return self.host.get_player_id()

    def get_color(self, player):
        if self.host.get_player_name() == player:
            return self.host.get_color()
        elif self.opponent.get_player_name() == player:
            return self.opponent.get_color()

    def get_question(self, question_type='default'):
        if question_type == 'default':
            return self.quiz.get_question()
        elif question_type == 'TTIK':
            return self.quiz.get_tipical_question(question_type)
        elif question_type == '2':
            return self.quiz.get_question2()
        else:
            ...

    def get_question_answer(self, question_id, user_answer):
        return self.quiz.get_answer(question_id, user_answer)

    def get_question_correct_answer(self, question_id):
        return self.quiz.get_correct_answer(question_id)

    def get_room_id(self):
        return self.lobby_id

    def get_lobby_id(self):
        return self.lobby_id

    def get_room_name(self):
        return self.lobby_name

    def get_lobby_name(self):
        return self.lobby_name

    def get_status(self):
        return self.status

    def get_host_id(self):
        return self.host.get_player_id()

    def get_host_name(self):
        return self.host.get_player_name()

    def get_opponent_id(self):
        return self.opponent.get_player_id()

    def get_opponent_name(self):
        return self.opponent.get_player_name()
