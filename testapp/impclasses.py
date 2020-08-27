from .testing.testing import QuestionsForTest

quest = QuestionsForTest()


def create_test():
    quest.__init__()


def fill_ans_list(lst):
    for i in range(len(quest.get_answers())):
        for j in range(len(quest.get_answers()[i])):
            if quest.get_answers()[i][j] in lst:
                quest.get_ans_list()[i].append(quest.get_answers()[i][j])


def get_mark(counter, lst):
    for k in range(20):
        if quest.get_ans_list()[k] == quest.get_answers()[k]:
            counter += 1
        else:
            lst.append(quest.get_questions_list()[k])
    return counter


def get_wrong_ans_id(lst):
    raw = ''
    for elements in lst:
        raw += str(elements[5]) + '; '
    return raw
