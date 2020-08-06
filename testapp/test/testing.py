from .test_interface import *
from ..impclasses import *


class Testing(TestInterface):

    def __init__(self):
        super(TestInterface, self).__init__()
        self.right_answers = self.create_right_answers_lst()

    def create_right_answers_lst(self):
        answers = list()
        for questions in quest:
            for ans in questions[3]:
                answers.append(ans)
        return answers

    def get_right_answers_lst(self):
        print(self.right_answers)
        return self.right_answers

    def check(self):
        pass

    def get_mark(self):
        pass
