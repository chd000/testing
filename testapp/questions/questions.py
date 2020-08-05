import random
from .question_chooser import *
from .question_interface import QuestionsInterface


class QuestionsForTest(QuestionsInterface):

    def __init__(self, pos):
        super(QuestionsInterface, self).__init__()
        self.variants = list()
        self.right_answers = list()
        self.question_list = self.create_variant_question_list()
        self.one_question = self.pick_question(pos)
        self.title = self.one_question[1]

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

    def pick_question(self, pos):
        return self.question_list[pos]

    def get_type(self):
        return self.one_question[0]

    def get_answers(self):
        for ans in self.one_question[2]:
            variant = (ans, ans)
            self.variants.append(variant)
        return self.variants

    def get_question(self):
        return self.title

    def get_right_answers(self):
        for ans in self.one_question[3]:
            answers = (ans, ans)
            self.right_answers.append(answers)
        return self.right_answers

    def print_question_info(self):
        for i in range(len(self.one_question)):
            print(self.one_question[i])