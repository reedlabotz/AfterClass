from app.accounts.forms import RegistrationFormNoUserName

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import redirect
from app.social.forms import UserForm, UserProfileForm, UserAvailabilityForm, UserCourseForm
from registration.views import register
from django.contrib.auth.decorators import login_required

# Create your views here.
def main(request):
   if request.user.is_authenticated():
      return redirect('/groups')
   else:
      return register(request,'app.accounts.regbackend.Backend','/',RegistrationFormNoUserName)

@login_required
def groups(request):
   return render_to_response('main.html',{'page':'groups'},context_instance=RequestContext(request))

@login_required
def explore(request):
   return render_to_response('main.html',{'page':'explore'},context_instance=RequestContext(request))

@login_required
def courses(request):
   courses = request.user.get_profile().courses.all()
   user_course_form = UserCourseForm()
   if request.POST:
      user_course_form = UserCourseForm(request.POST)
      if user_course_form.is_valid():
         user_course = user_course_form.save(commit=False)
         user_course.user = request.user.get_profile()
         user_course.save()
         if request.POST.get('add'):
            user_course_form = UserCourseForm()
            courses = request.user.get_profile().courses.all()
         else:
            return redirect('/dashboard')
      elif courses.count() > 0 and len(user_course_form.errors.items())== 6:
         return redirect('/dashboard')
   return render_to_response('main.html',{'page':'courses','courses':courses,'user_course_form':user_course_form},context_instance=RequestContext(request))


### Welcome views ###

@login_required
def welcome_account(request):
   user_form = UserForm(instance=request.user)
   user_profile_form = UserProfileForm(instance=request.user.get_profile())
   if request.POST:
      user_form = UserForm(request.POST,instance=request.user)
      user_profile_form = UserProfileForm(request.POST,instance=request.user.get_profile())
      if user_form.is_valid() and user_profile_form.is_valid():
         user_form.save()
         user_profile_form.save()
         return redirect('/welcome/availability')
   return render_to_response('welcome_account.html',{'user_form':user_form,'user_profile_form':user_profile_form},context_instance=RequestContext(request))

@login_required
def welcome_availability(request):
   user_availability_form = UserAvailabilityForm(instance=request.user.get_profile())
   days = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
   hours = ['12am','1am','2am','3am','4am','5am','6am','7am','8am','9am','10am','11am','12pm','1pm','2pm','3pm','4pm','5pm','6pm','7pm','8pm','9pm','10pm','11pm']

   if request.POST:
      user_availability_form = UserAvailabilityForm(request.POST,instance=request.user.get_profile())
      if user_availability_form.is_valid():
         user_availability_form.save()
         return redirect('/courses')
   return render_to_response('welcome_availability.html',{'user_availability_form':user_availability_form,'days':days,'hours':hours},context_instance=RequestContext(request))


### 500 error view ###

def error(request):
   return render_to_response('500.html',{},context_instance=RequestContext(request))
   