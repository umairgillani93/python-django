from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, template_name = 'main/home.html')

def info(request):
    return render(request, template_name = 'main/info.html')

def register(request):
    return render(request, template_name = 'main/register.html')

def login(request):
    return render(request, template_name = 'main/login.html')
