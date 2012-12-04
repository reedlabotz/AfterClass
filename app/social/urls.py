from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('',
   url(r'^groups/$','app.social.views.groups'),
   url(r'^groups/create/$','app.social.views.groups_create'),
   url(r'^groups/requests/(?P<id>\d+)/$','app.social.views.partner_request'),
   url(r'^explore/$','app.social.views.explore'),
   url(r'^explore/(?P<id>\d+)/$','app.social.views.explore_course'),
   url(r'^courses/$','app.social.views.courses'),
   url(r'^courses/add/$','app.social.views.courses_add'),
   url(r'^courses/drop/$','app.social.views.courses_drop'),

   ## first time
   url(r'^welcome/$','app.social.views.welcome'),
   url(r'^welcome/account/$','app.social.views.welcome_account'),
   url(r'^welcome/availability/$','app.social.views.welcome_availability'),
)


   