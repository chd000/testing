import json
from django.core import serializers
from ..models import Questions


def create_all_question_list():
    for elements in edited_questions:
        question_type = elements['fields']['quest_type']
        question = elements['fields']['quest']
        answers = elements['fields']['answers'].split(sep=';')
        right_answers = elements['fields']['right_answer'].split(sep=';')
        picture = elements['fields']['picture']
        all_questions_lst.append((question_type, question, answers, right_answers, picture))


questions = Questions.objects.all()
edited_questions = json.loads(serializers.serialize('json', questions, fields=('quest', 'answers', 'right_answer', 'quest_type', 'picture')))
all_questions_lst = list()

create_all_question_list()
