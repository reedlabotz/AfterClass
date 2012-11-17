from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('',
   url(r'^groups/$','app.social.views.groups'),
   url(r'^explore/$','app.social.views.explore'),
   url(r'^courses/$','app.social.views.courses'),

   ## first time
   url(r'^welcome$','app.social.views.welcome'),
   url(r'^welcome/account/$','app.social.views.welcome_account'),
   url(r'^welcome/availability/$','app.social.views.welcome_availability'),
)


   