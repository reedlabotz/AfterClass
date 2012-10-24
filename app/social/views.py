from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import redirect
from app.social.forms import UserForm, UserProfileForm, UserAvailabilityForm, UserCourseForm


# Create your views here.
def main(request):
   if request.user.is_authenticated():
      return redirect('/dashboard')
   return render_to_response('main.html',{},context_instance=RequestContext(request))

def dashboard(request):
   if request.user.first_name == "":
      return redirect('/dashboard/first/')
   if request.user.get_profile().monday_availability == "":
      return redirect('/dashboard/first/availability')
   if request.user.get_profile().courses.all().count() == 0:
      return redirect('/dashboard/first/courses')
   return render_to_response('main.html',{},context_instance=RequestContext(request))

def first_time(request):
   return render_to_response('first_time/main.html',{},context_instance=RequestContext(request))

def first_time_account(request):
   user_form = UserForm(instance=request.user)
   user_profile_form = UserProfileForm(instance=request.user.get_profile())
   if request.POST:
      user_form = UserForm(request.POST,instance=request.user)
      user_profile_form = UserProfileForm(request.POST,instance=request.user.get_profile())
      if user_form.is_valid() and user_profile_form.is_valid():
         user_form.save()
         user_profile_form.save()
         return redirect('/dashboard/first/availability')
   return render_to_response('first_time/account.html',{'user_form':user_form,'user_profile_form':user_profile_form},context_instance=RequestContext(request))

def first_time_availability(request):
   user_availability_form = UserAvailabilityForm(instance=request.user.get_profile())
   days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
   hours = ['8am','9am','10am','11am','12pm','1pm','2pm','3pm','4pm','5pm','6pm','7pm','8pm','9pm','10pm','11pm']

   if request.POST:
      user_availability_form = UserAvailabilityForm(request.POST,instance=request.user.get_profile())
      if user_availability_form.is_valid():
         user_availability_form.save()
         return redirect('/dashboard/first/courses')
   return render_to_response('first_time/availability.html',{'user_availability_form':user_availability_form,'days':days,'hours':hours},context_instance=RequestContext(request))

def first_time_courses(request):
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
   return render_to_response('first_time/courses.html',{'courses':courses,'user_course_form':user_course_form},context_instance=RequestContext(request))

def courses(request):
   return render_to_response('main.html',{},context_instance=RequestContext(request))

def friends(request):
   return render_to_response('main.html',{},context_instance=RequestContext(request))

def account(request):
   return render_to_response('main.html',{},context_instance=RequestContext(request))
   