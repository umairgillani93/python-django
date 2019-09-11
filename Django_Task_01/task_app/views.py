from django.shortcuts import render
from task_app.models import Question, Choice
from django.http import HttpResponse

def home(request):
    return render(request, 'task_app/home.html')

def aboutus(request):
    return render(request, 'task_app/aboutus.html')

def login(request):
    return render(request, 'task_app/login.html')

def register(request):
    return render(request, 'task_app/register.html')

def question_list(reqeust):
    latest_question_list = Question.objects.all()
    output = ','.join([q.question_text for q in latest_question_list])
    pub_date = '---'.join([q.question_text for q in latest_question_list])
    return HttpResponse(output, pub_date)

def Choice_list(request):
    choices_list = Choice.choice_set.all()
    output = ','.join([c.choice_text for c in choices_list])
    return HttpResponse(output)
