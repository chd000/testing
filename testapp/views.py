from django.contrib import messages
from .forms import UserRegistrationForm, CBForm, SeqForm
from .models import Questions
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
    user_answers_list = request.GET.getlist('list[]')
    ans_list = list()
    for j in range(20):
        var_list = list()
        ans_list.append(var_list)
    print('Лист правильных ответов: {}'.format(quest.get_answers()))
    for i in range(len(quest.get_answers())):
        for j in range(len(quest.get_answers()[i])):
            if quest.get_answers()[i][j] in user_answers_list:
                ans_list[i].append(quest.get_answers()[i][j])
    for k in range(20):
        if ans_list[k] == quest.get_answers()[k]:
            print(ans_list[k])
            quest.increase_counter()
    print('Ваши ответы: {}'.format(ans_list))
    context = {
        'mark': quest.get_counter()
    }
    return render(request, 'main/result.html', context)
