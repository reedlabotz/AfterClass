from django import forms
from registration.forms import RegistrationFormUniqueEmail
from django.contrib.auth.models import User

class RegistrationFormNoUserName(RegistrationFormUniqueEmail):
    """
    A registration form that only requires the user to enter their e-mail 
    address and password. The username is automatically generated
    This class requires django-registration to extend the 
    RegistrationFormUniqueEmail
    """ 
    username = forms.CharField(widget=forms.HiddenInput, required=False)

    def clean_username(self):
        "This function is required to overwrite an inherited username clean"
        return self.cleaned_data['username']

    def clean(self):
        if not self.errors:
            self.cleaned_data['username'] = '%s%s' % (self.cleaned_data['email'].split('@',1)[0], User.objects.count())
        super(RegistrationFormNoUserName, self).clean()
        return self.cleaned_data