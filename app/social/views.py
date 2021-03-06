from app.accounts.forms import RegistrationFormNoUserName

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import redirect, get_object_or_404
from app.social.forms import UserForm, UserProfileForm, UserAvailabilityForm, UserCourseForm
from django.contrib.auth.decorators import login_required,user_passes_test
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.forms.util import ErrorList
from django.db import IntegrityError
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import json
from datetime import datetime

from registration.views import register

from app.social.models import UserProfile, UserCourse, PartnerRequest, Circle, CircleUser, CircleAction

from app.social.helper import isWelcome

# Create your views here.
def main(request):
   if request.user.is_authenticated():
      return redirect('/groups')
   else:
      return register(request,'app.accounts.regbackend.Backend','/',RegistrationFormNoUserName)

@login_required
@user_passes_test(isWelcome, login_url='/welcome')
def groups(request):
   groups = request.user.circle_set.all()
   requests = request.user.partner_request_user.all()
   return render_to_response('groups.html',{'page':'groups','groups':groups,'requests':requests},context_instance=RequestContext(request))

@login_required
@user_passes_test(isWelcome, login_url='/welcome')
def groups_details(request,id):
   group =  get_object_or_404(request.user.circle_set,id=id)
   circleuser = request.user.circleuser_set.get(circle=group)
   if request.POST:
      if len(request.POST.get('message')) > 0:
         action = CircleAction(user=request.user,circle=group,type='c',text=request.POST.get('message'))
         action.save()
      if request.POST.get('video') is not None:
         circleuser.video = request.POST.get('video') == "Yes"
         circleuser.last_video = datetime.now()
         circleuser.save()
      if(request.is_ajax()):
         return HttpResponse(json.dumps({'success':'Message sent'}), mimetype="application/json")
   actions = group.circleaction_set.all()
   people = map(lambda u: u.user.usercourse_set.get(course=group.course),group.circleuser_set.exclude(user=request.user))

   request_video = not circleuser.video
   if request_video:
      request_video = group.circleaction_set.filter(created__gt=circleuser.last_video).count() > 10
      print  group.circleaction_set.filter(created__gt=circleuser.last_video).count()
   return render_to_response('groups_details.html',{'page':'groups','group':group,'actions':actions,'people':people,'profile':request.user.get_profile(),'request_video':request_video},context_instance=RequestContext(request))

@login_required
@user_passes_test(isWelcome, login_url='/welcome')
@require_POST
def groups_create(request):
   usercourse = get_object_or_404(request.user.usercourse_set,id=request.POST.get('usercourse_id'))
   other = get_object_or_404(usercourse.course.usercourse_set,id=request.POST.get('user_id'))
   
   partner_request = PartnerRequest(owner=request.user,user=other.user,course=usercourse.course).save()

   if(request.is_ajax()):
      return HttpResponse(json.dumps({'success':'Request sent'}), mimetype="application/json")
   else:
      messages.add_message(request,messages.SUCCESS,'Request sent.')

      return render_to_response('main.html',{'page':'groups'},context_instance=RequestContext(request))

@login_required
@user_passes_test(isWelcome, login_url='/welcome')
def partner_request(request,id):
   partner_request = get_object_or_404(request.user.partner_request_user,id=id)
   if request.POST:
      if request.POST.get('accept') == "true":
         circle = Circle(course=partner_request.course)
         circle.save()
         circleuser_owner = CircleUser(circle=circle,user=partner_request.owner)
         circleuser_owner.save()
         circleuser_user = CircleUser(circle=circle,user=partner_request.user)
         circleuser_user.save()
         messages.add_message(request,messages.SUCCESS,"Request accepted, a group has been created.")
         partner_request.delete()
         return redirect('/groups')
      if request.POST.get('reject') == "true":
         partner_request.deleted = True
         partner_request.save()
         messages.add_message(request,messages.SUCCESS,"Request rejected.")
         return redirect('/groups')
   return render_to_response('partner_request.html',{'page':'groups','partner_request':partner_request},context_instance=RequestContext(request))

@login_required
@user_passes_test(isWelcome, login_url='/welcome')
def explore(request):
   courses = request.user.usercourse_set.all()
   return render_to_response('explore.html',{'page':'explore','courses':courses},context_instance=RequestContext(request))

@login_required
@user_passes_test(isWelcome, login_url='/welcome')
def explore_course(request,id):
   usercourse = get_object_or_404(request.user.usercourse_set,id=id)
   course = usercourse.course
   people = course.usercourse_set.exclude(user=request.user)
   paginator = Paginator(people, 25)

   page = request.GET.get('page')
   try:
      people = paginator.page(page)
   except PageNotAnInteger:
      # If page is not an integer, deliver first page.
      people = paginator.page(1)
   except EmptyPage:
      # If page is out of range (e.g. 9999), deliver last page of results.
      people = paginator.page(paginator.num_pages)

   return render_to_response('explore_course.html',{
      'page':'explore',
      'user': request.user,
      'people':people,
      'usercourse':usercourse
      },context_instance=RequestContext(request))

@login_required
@user_passes_test(isWelcome, login_url='/welcome')
def courses(request):
   courses = request.user.usercourse_set.all()
   return render_to_response('courses.html',{'page':'courses','courses':courses},context_instance=RequestContext(request))

@login_required
@user_passes_test(isWelcome, login_url='/welcome')
def courses_add(request):
   user_course_form = UserCourseForm()
   if request.POST:
      user_course_form = UserCourseForm(request.POST)
      if user_course_form.is_valid():
         user_course = user_course_form.save(commit=False)
         user_course.user = request.user
         try:
            user_course.save()
            messages.add_message(request, messages.SUCCESS, "Course Added.")
            return redirect('/explore/%d/'%user_course.id)
         except IntegrityError: 
            user_course_form._errors["course"] = ErrorList([u'You are already enrolled in that course'])
   return render_to_response('courses_add.html',{'page':'courses','user_course_form':user_course_form},context_instance=RequestContext(request))

@login_required
@user_passes_test(isWelcome, login_url='/welcome')
@require_POST
def courses_drop(request):
   id = request.POST.get('usercourse_id')
   course = get_object_or_404(request.user.usercourse_set, id=id)
   course.delete()
   messages.add_message(request, messages.SUCCESS, "Course dropped.")
   return redirect('/courses')


### Welcome views ###
@login_required
def welcome(request):
   if len(request.user.first_name) > 0:
      return redirect('/welcome/availability')
   return redirect('/welcome/account')

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
   