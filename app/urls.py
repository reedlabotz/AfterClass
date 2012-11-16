from django.conf.urls import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
   url(r'^$', 'app.social.views.main'),
   url(r'^dashboard/$','app.social.views.dashboard'),
   url(r'^courses/$','app.social.views.dashboard'),
   url(r'^friends/$','app.social.views.friends'),

   url(r'^account/$','app.social.views.account'),

   ## first time
   url(r'^dashboard/first/$','app.social.views.first_time'),
   url(r'^dashboard/first/account/$','app.social.views.first_time_account'),
   url(r'^dashboard/first/availability/$','app.social.views.first_time_availability'),
   url(r'^dashboard/first/courses/$','app.social.views.first_time_courses'),

   ## registration
   url(r'^', include('app.accounts.urls')),
)

handler500 = 'app.social.views.error'

if settings.DEBUG == True:
   from django.contrib.staticfiles.urls import staticfiles_urlpatterns
   urlpatterns += staticfiles_urlpatterns()