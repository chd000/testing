import json

from django.contrib import messages
from .forms import UserRegistrationForm, CBForm, SeqForm
from .models import Questions
from .models import Questions
from .questions.questions import QuestionsForTest
from django.shortcuts import redirect, render
from .impclasses import *


def registration(request):
    error = ''
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Аккаунт успешно зарегестрирован')
            return redirect('home')
        else:
            error = ' Форма была неверной '

    form = UserRegistrationForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'registration/registration.html', context)


def test(request):
    question = quest.get_questions_list()
    error = ''
    if request.method == 'POST':
        cbform = CBForm(request.POST)
        seqform = SeqForm(request.POST)
        if cbform.is_valid() and seqform.is_valid():
            cbform.save()
            seqform.save()
        else:
            error = ' Форма была неверной '
    cbform = CBForm()
    seqform = SeqForm()
    context = {
        'numbers': range(20),
        'cbform': cbform,
        'seqform': seqform,
        'error': error,
        'questions': question,
    }
    return render(request, 'main/test.html', context)


def index(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'num_visits': num_visits})


def quest_list(request):
    question_query = Questions.objects.all()
    return render(request, 'main/list.html', {'title': 'Страница со списком вопросов', 'questions': question_query})


def result(request):
    # ver_system = Testing()
    # ver_system.get_right_answers_lst()
    user_answers_list = request.GET.get('list')
    list_ans = list()
    leng = str(user_answers_list)
    for i in range(len(quest.get_answers())):
        if list_ans[i] == quest.get_answers()[i]:
            quest.increase_counter()
    context = {
        'mark': quest.get_counter()
    }
    return render(request, 'main/result.html', context)
