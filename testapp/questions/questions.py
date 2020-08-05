import random
from .question_chooser import *
from .question_interface import QuestionsInterface


class QuestionsForTest(QuestionsInterface):

    def __init__(self):
        super(QuestionsInterface, self).__init__()
        self.question_list = self.create_variant_question_list()

    def create_variant_question_list(self):
        question_list = list()
        counter = 0
        for i in range(len(all_questions_lst)):
            rnd = random.randint(1, len(all_questions_lst) - 1)
            question_list.append(all_questions_lst[rnd])
            all_questions_lst.remove(all_questions_lst[rnd])
            counter += 1
            if counter == 20:
                break
        create_all_question_list()
        return question_list

    def get_questions_list(self):
        return self.question_list
