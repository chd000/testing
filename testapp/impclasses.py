from .testing.testing import QuestionsForTest

quest = QuestionsForTest()


def fill_ans_list(lst):
    for i in range(len(quest.get_answers())):
        for j in range(len(quest.get_answers()[i])):
            if quest.get_answers()[i][j] in lst:
                quest.get_ans_list()[i].append(quest.get_answers()[i][j])


def get_mark(counter):
    for k in range(20):
        if quest.get_ans_list()[k] == quest.get_answers()[k]:
            counter += 1
        else:
            quest.get_wrong_answers_list().append(quest.get_questions_list()[k])
    return counter
