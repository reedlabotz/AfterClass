from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.models import User

from registration import signals
from registration.forms import RegistrationForm
from registration.models import RegistrationProfile


from registration.backends import simple


class Backend(simple.SimpleBackend):
    def register(self, request, **kwargs):
        email, password = kwargs['email'], kwargs['password1']
        username = email
        User.objects.create_user(username, email, password)
        
        # authenticate() always has to be called before login(), and
        # will return the user we just created.
        new_user = authenticate(username=username, password=password)
        login(request, new_user)
        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=request)
        return new_user