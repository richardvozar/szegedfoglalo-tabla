import sys


class Player:
    def __init__(self,
                 player_name,
                 player_id,
                 player_point,
                 color,
                 host,
                 opponent,
                 side,
                 image):
        self.player_name = player_name
        self.player_id = player_id
        self.player_point = player_point
        self.color = color
        self.host = host
        self.opponent = opponent
        self.side = side
        self.connected = False
        self.last_answer = []
        self.last_point = []
        self.last_answer_time = ""
        self.last_answer_time_answer = ""
        self.distance = 10000
        self.image=f"../static/images/profpic{image}.png"
        print(f"konstriktor {self.last_answer_time==''}")

    def get_image(self):
        return self.image
    def set_last_answer_distance(self, distance=10000):
        self.distance = distance

    def get_last_answer_distance(self):
        return self.distance

    ######################
    def has_last_answer_time(self):
        if self.last_answer_time != "":
            return True
        else:
            return False

    def get_last_answer_time_answer(self):
        return self.last_answer_time_answer

    def set_last_answer_time(self, time,answer):
        self.last_answer_time = time
        self.last_answer_time_answer=answer

    def get_last_answer_time(self):
        return self.last_answer_time

    ######################
    def get_side(self):
        return self.side

    def is_host(self):
        return self.host

    def is_opponent(self):
        return self.opponent

    def is_connected(self):
        return self.connected

    def get_color(self):
        return self.color

    def get_player_point(self):
        return self.player_point

    def get_player_id(self):
        return self.player_id

    def get_player_name(self):
        return self.player_name

    def has_last_point(self):
        if len(self.last_point) == 0:
            return False
        elif len(self.last_point) == 1:
            return True
        else:
            print("HIBA def has_last_point(self):")
            sys.exit()

    def get_last_point(self):
        if len(self.last_point) == 0:
            print("HIBA if len(self.last_point)==0:")
        return self.last_point[0]

    def add_last_point(self, point):
        if len(self.last_point) > 0:
            self.last_point.pop()
            print("HIBA if def add_last_point(self, point):")
        self.last_point.append(point)

    def del_last_point(self):

        if len(self.last_point) > 0:
            self.last_point.pop()
        else:
            print("HIBA def del_last_point(self):")

    def has_last_answer(self):
        if len(self.last_answer) == 0:
            return False
        elif len(self.last_answer) == 1:
            return True
        else:
            print("HIBA def has_last_answer(self):")
            sys.exit()

    def get_last_answer(self):
        if len(self.last_answer) == 0:
            print("HIBA if len(self.last_answer)==0:")
        return self.last_answer[0]

    def add_last_answer(self, answer):
        self.last_answer = []
        # if len(self.last_answer) > 0:
        #     self.last_answer.pop()
        #     print("HIBA if def add_last_answer(self, answer):")
        self.last_answer.append(answer)

    def del_last_answer(self):
        self.last_answer = []
        print("self.last_answer=[]")
        # if len(self.last_point) > 0:
        #     self.last_answer.pop()
        # else:
        #     print("HIBA def del_last_answer(self):")

    def set_connect(self):
        self.connected = True

    def set_disconnect(self):
        self.connected = False

    def reset_point(self):
        self.player_point=0

    def set_player_point(self, point):
        self.player_point += point

    def __getitem__(self, key):
        return getattr(self, key)

    def __str__(self):
        return f"""
        {self.player_name}        
        {self.player_id}
        {self.player_point}
        {self.color}
        {self.host}
        {self.opponent}
        {self.side}
        {self.connected}
        {self.last_answer}
        {self.last_point}
        {self.last_answer_time}
        """
