from django.shortcuts import render
from django.http import HttpResponse

from appTwo.forms import NewUserForm


# Create your views here.
def index(request):
    return render(request, 'appTwo/index.html')

def users(request):

    form = NewUserForm() # instantiating the NewUserForm we just created in forms.py

    if request.method == 'POST': # checks if data is gettin submitted from User
        form = NewUserForm(request.POST) # declare the request to be 'POST'

        if form.is_valid(): # check if there isn't anything wrong with our form
            form.save(commit = True) # save the form, and commit changes to the database

            return index(request) # return the index page! Basically will take you back to the home page

        else:
            print('ERROR! FORM INVALID!')

    return render(request, 'appTwo/users.html', {'form':form})
