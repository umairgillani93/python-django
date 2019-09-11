from django import forms
from django.core import validators

# DJANGO'S built-in validators!
#def check_for_z(value): # Own validator, checks if a letter starts off with 'z'
    # value -> keyword, makes Django understand that it's a Validator function
    #if value[0].lower() != 'z':
        #raise forms.ValidationError("NAME NEEDS TO START WITH Z!")

class FormName(forms.Form): # inheriting from forms.Form
    name = forms.CharField() # name field in form
    email = forms.EmailField() # email field in form
    verify_email = forms.EmailField(label = 'Enter Email again!')
    text = forms.CharField(widget = forms.Textarea) # random text area field in the form
    #botcatcher = forms.CharField(required = False, widget = forms.HiddenInput,
                                #validators = [validators.MaxLengthValidator(0)]) # bot cather field
    # to check if there's any Robot trying to sneak through our website!

    # Remember! CSRF security feature helps maintain the security of a website
    # it actually has this randome code generated value, for the user at front end
    # and Django is gonna check if it matches with the back end
    # and makes sure that the input user is putting is not going to to any other website

    # But! the input we made is botcatcher, which is given some name and 'id'
    # and it's type is hidden
    # and basically what's gonna happen is, if a Bot is going to visit your page,
    # they will not look at the actual website, but they're gonna look directly into
    # the HTML, and then they're gonna automatically fill up the value attributes (form fields)
    # and finally submit the form!

    # Now in order to catch the Bot, we're gonna set some validators, that check the validation of the form,
    # for that, we're gonna make the following function:

    # def clean_botcatcher(self):
        # botcatcher = self.cleaned_data['botcatcher'] # checks if the botchecker field has got some input
        # if len(botcatcher) > 0:
            # raise forms.ValidationError("GOTCHA BOT!") # raises an Error of a Bot trying to sneak through the website!

        # return botcatcher

    def clean(self): # single clean method for entire form at once
        all_clean_data = super().clean() # returns all the cleaned data in the form
        email = all_clean_data['email']
        v_email = all_clean_data['verify_email']

        if email != v_email:
            raise forms.ValidationError("MAKE SURE THE EMAILS MATCH!")
