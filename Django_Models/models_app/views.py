from django.shortcuts import render
from models_app.models import Topic, Webpage, AccessRecord

# Create your views here.
def index(request):

    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    #my_dict = {'insert content':'I am from index page!'}
    return render(request, 'models_app/index.html', context = date_dict)
