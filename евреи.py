
import json
class Question_list:
    def __init__(self):
        self.question_list = []
        self.timer = 000
        self.right_answers = 0
    def add_quest(self,question):
        if question:
            self.question_list.append(question)
    def delete_quest (self,question):
        if question in self.question_list:
            self.question_list.remove(question)
    def get_questions(self):
        for quest in self.question_list:
            print(quest.text_question)


def print(param):
    pass


class Question:
    def __init__(self,text_question,right_answer,wrong_answer1,wrong_answer2,wrong_answer3):
        self.text_question=text_question
        self.right_answer=right_answer
        self.wrong_answer1=wrong_answer1
        self.wrong_answer2=wrong_answer2
        self.wrong_answer3=wrong_answer3
    def check_answer(self,user_answer):
        if user_answer == self.right_answer:
            print("pravilno")
        else:
            print("wrong")
q1 = Question(
    "кто великий правитель",
    "Джордж Вашингтон",
    "Адольф Гитлер",
    "Мистер Бист",
    "Джо Байден"
)
q2 = Question(
    "кто был президентом америки во время войны за независимость?",
    "Джордж Вашингтон",
    "Адольф Гитлер",
    "Мистер Бист",
    "Джо Байден"
)
q3 = Question(
    "как закрыть файл",
    "Выкинуть компютер",
    "альт + ф4",
    "Зжеть дом",
    "Стать Гитлером"
)
q4 = Question(
    "как не завоевать всю европу ",
    "Не поступать в художку",
    "Быть художником",
    "Родиться",
    "Абра Кадабра"
)
q5 = Question(
    "как какать",
    "скибиди туалет",
    "Быть гитлером",
    "Родиться сталином",
    "Абра Кадабра в жопу палка"
)
q6 = Question(
    "ААА НА меня напал НЕГР что делать",
    "Заставить его работать",
    "Быть рабовладельцом",
    "Работать",
    "я черный"
)
q7 = Question(
    "масовый рострел в каком году был",
    "1939",
    "1941",
    "1942",
    "1943"
)
q8 = Question(
    "как не стать какашкой",
    "Не поступать в скибиди туалет",
    "Быть художником с стальными шарами",
    "Родиться комунягой",
    "Абра неграбрада"
)
q9 = Question(
    "как не стать знаком вопросом",
    "Не поступать в логику",
    "ДЕТКА ВОТ МОЙ ВУНДЕРФАУСТ СМОТРИ",
    "Родиться мудатоном",
    "Абра Кадабра кароче мне лень"
)
q10 = Question(
    "как устраивать масовые убийства",
    "Не поступать в художку",
    "Быть художником",
    "Родиться",
    "Абра Кадабра"
)
victorina = Question_list()
victorina.add_quest(q1)
victorina.add_quest(q2)
victorina.add_quest(q3)
victorina.add_quest(q4)
victorina.add_quest(q5)
victorina.add_quest(q6)
victorina.add_quest(q7)
victorina.add_quest(q8)
victorina.add_quest(q9)
victorina.add_quest(q10)
(victorina.get_questions())
# with open("logical.json","w",encoding="UTF-8") as file:
#      json.dump({"name":"kostantin"},file)
with open("logical.json", "r", encoding="UTF-8") as file:
    a = json.load(file)
print(a["name"])