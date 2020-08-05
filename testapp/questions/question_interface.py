from abc import ABC, abstractmethod


class QuestionsInterface(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_questions_list(self):
        pass

    @abstractmethod
    def create_variant_question_list(self):
        pass
