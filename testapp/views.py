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
    create_test()
    return render(request, 'main/index.html', {'title': 'Главная страница сайта'})


def result(request):
    counter = 0
    wrong_ans = list()
    question_query = Questions.objects.all()
    user_answers_list = request.GET.getlist('list[]')
    fill_ans_list(user_answers_list)
    mark = get_mark(counter, wrong_ans)
    raw = get_wrong_ans_id(wrong_ans)
    percent = mark * 5
    # for element in wrong_ans:
    #    this_question = Questions.objects.get(id=element[5])
    #    if this_question.quest in element[1]:
    #        this_question.answered_wrong += 1
    #        this_question.save()
    if mark > 15:
        request.user.category = True
    test_result = ResultTable(email=request.user.email, last_name=request.user.last_name,
                              first_name=request.user.first_name, middle_name=request.user.middle_name,
                              working_at=request.user.working_at, mark=mark, wrong_answers=raw,
                              right_ans_percent=percent)
    test_result.save()
    context = {
        'mark': mark,
        'percent': percent,
        'wrong': wrong_ans,
        'img': question_query
    }
    return render(request, 'main/result.html', context)
