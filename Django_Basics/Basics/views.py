from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1> Hello World! </h1>")

def login(request):
    return HttpResponse("<h1> Login Page </h1>")

def register(request):
    return HttpResponse('<h1> Registration page! </h1>')

def index1(request):
    return render(request, 'Basics/index1.html')

def login1(request):
    return render(request, 'Basics/login1.html')

def register1(request):
    return render(request, 'Basics/register1.html')
