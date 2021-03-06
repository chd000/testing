from abc import ABC, abstractmethod


class QuestionsInterface(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def create_ans_list(self):
        pass

    @abstractmethod
    def get_ans_list(self):
        pass

    @abstractmethod
    def get_questions_list(self):
        pass

    @abstractmethod
    def create_variant_question_list(self):
        pass

    @abstractmethod
    def create_right_answers(self):
        pass

    @abstractmethod
    def get_answers(self):
        pass

    @abstractmethod
    def get_wrong_answers_list(self):
        pass