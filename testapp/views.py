from django.contrib import messages
from .forms import UserRegistrationForm
from .models import Questions, ResultTable
from django.shortcuts import redirect, render, HttpResponseRedirect
from .impclasses import *
from .testing.question_chooser import *


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
    counter = 0
    question_query = Questions.objects.all()
    user_answers_list = request.GET.getlist('list[]')
    fill_ans_list(user_answers_list)
    mark = get_mark(counter)
    percent = mark * 5

    test_result = ResultTable(email=request.user.email, last_name=request.user.last_name,
                              first_name=request.user.first_name, middle_name=request.user.middle_name, mark=counter, right_ans_percent=percent)
    test_result.save()
    context = {
        'mark': mark,
        'percent': percent,
        'wrong': quest.get_wrong_answers_list(),
        'img': question_query
    }
    # return HttpResponseRedirect('http://127.0.0.1:8000/result')
    return render(request, 'main/result.html', context)
