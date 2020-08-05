from django.contrib import messages
from .forms import UserRegistrationForm, CBForm, SeqForm
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
    form = None
    error = ''
    if request.method == 'POST':
        if quest.get_type() == '1':
            form = CBForm(request.POST)
        elif quest.get_type() == '2':
            form = SeqForm(request.POST)
            if form.is_valid():
                form.save()
            else:
                error = ' Форма была неверной '
    if quest.get_type() == '1':
        form = CBForm()
    elif quest.get_type() == '2':
        form = SeqForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/test.html', context)


def index(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'num_visits': num_visits})


def quest_list(request):
    question_query = Questions.objects.all()
    return render(request, 'main/list.html', {'title': 'Страница со списком вопросов', 'questions': question_query})