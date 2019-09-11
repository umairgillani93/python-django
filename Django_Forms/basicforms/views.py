from django.shortcuts import render
from basicforms import forms # import forms.py in order to use it in views.py file

# creating views
def index(request):
    return render(request, 'basicforms/index.html')

def forms_name_view(request):
    form = forms.FormName()

    if request.method == 'POST': # Lets the Django know that the form is getting accepted from user
        form = forms.FormName(request.POST)

        if form.is_valid():
            # Essentially checks that if form is valid on submission
            # DOES SOME CODE
            print('VALIDATION SUCCESS!')
            print('Name: ' + form.cleaned_data(['name']))
            print('Email: ' + form.cleaned_data(['email']))
            print('Text: ' + form.cleaned_data(['text']))

    return render(request, 'basicforms/forms_page.html', context = {'form':form})
