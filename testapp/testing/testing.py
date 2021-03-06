import random
from .question_chooser import *
from .testing_interface import QuestionsInterface


class QuestionsForTest(QuestionsInterface):

    def __init__(self):
        super(QuestionsInterface, self).__init__()
        self.question_list = self.create_variant_question_list()
        self.right_answers = self.create_right_answers()
        self.user_ans_list = self.create_ans_list()
        self.wrong_answers_list = list()
        self.counter = 0

    def create_variant_question_list(self):
        question_list = list()
        count = 0
        for i in range(len(all_questions_lst)):
            if count == 20:
                break
            rnd = random.randint(1, len(all_questions_lst) - 1)
            if all_questions_lst[rnd] not in question_list:
                question_list.append(all_questions_lst[rnd])
                count += 1
        create_all_question_list()
        return question_list

    def get_questions_list(self):
        return self.question_list

    def create_right_answers(self):
        right_ans = list()
        for answers in self.question_list:
            variants = list()
            for ans in answers[3]:
                variants.append(ans)
            right_ans.append(variants)
        return right_ans

    def create_ans_list(self):
        ans_list = list()
        for count in range(20):
            var_list = list()
            ans_list.append(var_list)
        return ans_list

    def get_ans_list(self):
        return self.user_ans_list

    def get_answers(self):
        return self.right_answers

    def get_wrong_answers_list(self):
        return self.wrong_answers_list
