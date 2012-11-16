from django.forms import ModelForm,ValidationError
from django import forms
from app.social.models import UserProfile, UserCourse
from django.contrib.auth.models import User

class UserProfileForm(ModelForm):
   class Meta:
      model = UserProfile
      fields = ['age','gender','person_type','learning_style','interest']
      required = fields

class UserForm(ModelForm):
   def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
   class Meta:
      model = User
      fields = ['first_name','last_name']

class UserAvailabilityForm(ModelForm):
  class Meta:
      model = UserProfile
      fields = ['monday_availability','tuesday_availability','wednesday_availability','thursday_availability','friday_availability','saturday_availability','sunday_availability']
      widgets = {
        'monday_availability': forms.HiddenInput(),
        'tuesday_availability': forms.HiddenInput(),
        'wednesday_availability': forms.HiddenInput(),
        'thursday_availability': forms.HiddenInput(),
        'friday_availability': forms.HiddenInput(),
        'saturday_availability': forms.HiddenInput(),
        'sunday_availability': forms.HiddenInput()
      }

class UserCourseForm(ModelForm):
  class Meta:
    model = UserCourse
    exclude = ['user']
