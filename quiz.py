import time
import random
from read_questions import ReadQuestionsJson

class Quiz:
    def __init__(self, ):
        self.read_questions_json = ReadQuestionsJson()

        self.questions = self.read_questions_json.read_questions()
        self.questions2 = self.read_questions_json.read_questions('questions2')
        self.AJTK = self.read_questions_json.read_questions('AJTK')
        self.GTK = self.read_questions_json.read_questions('GTK')
        self.BTK = self.read_questions_json.read_questions('BTK')
        self.SZAOK = self.read_questions_json.read_questions('SZAOK')
        self.TTIK = self.read_questions_json.read_questions('TTIK')

        self.asked_question = list()
        self.current_question = list()

    def wait(self):
        while self.current_question:
            time.sleep(1)

    def get_questions(self):
        print(self.questions)

    def get_question(self):
        question = self.questions.pop()
        self.asked_question.append(question)
        return question

    def get_question2(self):
        question = self.questions2.pop()
        self.asked_question.append(question)
        return question

    def get_answer(self, question_id, user_answer):
        for asked in self.asked_question:
            if question_id == asked["question_id"]:
                return asked["Cor_answ"] == user_answer
        return False

    def get_correct_answer(self, question_id):
        for asked in self.asked_question:
            if question_id == asked["question_id"]:
                return asked["Cor_answ"]
        return False

    def get_tipical_question(self, type):
        if type == 'AJTK':
            try:
                question = self.AJTK.pop()
                self.asked_question.append(question)
                return question
            except:
                return "AJTK HIBA"
        elif type == 'BTK':
            try:
                question = self.BTK.pop()
                self.asked_question.append(question)
                return question
            except:
                return "BTK HIBA"
        elif type == 'GTK':
            try:
                question = self.GTK.pop()
                self.asked_question.append(question)
                return question
            except:
                return "GTK HIBA"
        elif type == 'SZAOK':
            try:
                question = self.SZAOK.pop()
                self.asked_question.append(question)
                return question
            except:
                return "SZAOK HIBA"
        elif type == 'TTIK':
            try:
                question = self.TTIK.pop()
                self.asked_question.append(question)
                return question
            except:
                return "TTIK HIBA"

    def shuffle_questions(self):
        random.shuffle(self.questions)
        random.shuffle(self.questions2)
        random.shuffle(self.AJTK)
        random.shuffle(self.BTK)
        random.shuffle(self.GTK)
        random.shuffle(self.TTIK)
