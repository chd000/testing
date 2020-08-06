from abc import ABC, abstractmethod


class TestInterface(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def create_right_answers_lst(self):
        pass

    @abstractmethod
    def get_right_answers_lst(self):
        pass

    @abstractmethod
    def check(self):
        pass

    @abstractmethod
    def get_mark(self):
        pass
