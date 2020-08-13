from django.contrib import messages
from .forms import UserRegistrationForm
from .models import Questions, ResultTable
from django.shortcuts import redirect, render
from .impclasses import *
from .testing.question_chooser import *
from django.template.response import TemplateResponse


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
    question_query = Questions.objects.all()
    question = quest.get_questions_list()
    context = {
        'img': question_query,
        'numbers': range(20),
        'counter': 1,
        'testing': question,
    }
    return render(request, 'main/test.html', context)


def index(request):
    quest.__init__()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта'})


def result(request):
    user_answers_list = request.GET.getlist('list[]')
    for i in range(len(quest.get_answers())):
        for j in range(len(quest.get_answers()[i])):
            if quest.get_answers()[i][j] in user_answers_list:
                quest.get_ans_list()[i].append(quest.get_answers()[i][j])
    counter = 0
    for k in range(20):
        if quest.get_ans_list()[k] == quest.get_answers()[k]:
            counter += 1
    session_user = ResultTable.objects.filter(email=request.user.email)
    if session_user.exists():
        person = ResultTable.objects.get(email=request.user.email)
        person.mark = counter
        person.save()
    else:
        test_result = ResultTable(email=request.user.email, last_name=request.user.last_name,
                                  first_name=request.user.first_name, mark=counter)
        test_result.save()
    context = {
        'mark': counter
    }
    # response = redirect('http://127.0.0.1:8000/result')
    # return response
    return render(request, 'main/result.html', context)
