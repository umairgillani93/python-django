from django import forms
from appTwo.models import User

class NewUserForm(forms.ModelForm):
    class Meta: # creating meta class to apply operations
        model = User # declare the model you are working on
        fields = '__all__' # for using all the fields of model User

        # Lets now go ahead and connect it to views.py
