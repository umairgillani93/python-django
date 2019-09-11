from django.shortcuts import render
from Django.Django_Models.models_app.models import Topic, Webpage, AccessRecord

# Create your views here.
def index(request):

    webpages_list =
    my_dict = {'insert content':'I am from views.py/MTV_app'}
    return render(request, 'MTV_app/index.html', context = my_dict)
