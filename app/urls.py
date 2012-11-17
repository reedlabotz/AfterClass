from django.conf.urls import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
   url(r'^$', 'app.social.views.main'),

   ## social app
   url(r'', include('app.social.urls')),

   ## registration
   url(r'', include('app.accounts.urls')),
)

handler500 = 'app.social.views.error'

if settings.DEBUG == True:
   from django.contrib.staticfiles.urls import staticfiles_urlpatterns
   urlpatterns += staticfiles_urlpatterns()