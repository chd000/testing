from abc import ABC, abstractmethod


class QuestionsInterface(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def pick_question(self, pos):
        pass

    @abstractmethod
    def get_type(self):
        pass

    @abstractmethod
    def get_answers(self):
        pass

    @abstractmethod
    def get_question(self):
        pass

    @abstractmethod
    def get_right_answers(self):
        pass

    @abstractmethod
    def print_question_info(self):
        pass

    @abstractmethod
    def create_variant_question_list(self):
        pass