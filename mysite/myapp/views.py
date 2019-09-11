from django.shortcuts import render

# to render a template we do the following steps
# add the application configuration to the installed applications list in settings.py file under
# the project directory
# Then, we to import render method, from django.shortcuts
# Then, pass in request and directory name e.g myapp/home.html as arguments in render method



def home(request):
    return render(request, 'myapp/home.html')

def about(request):
    return render(request, 'myapp/about.html')

def login(request):
    return render(request, 'myapp/login.html')
