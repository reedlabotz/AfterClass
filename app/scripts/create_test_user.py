import sys,os
sys.path.append(os.path.abspath('..'))

from django.core.management import setup_environ 
import settings 
setup_environ(settings)

from django.contrib.auth.models import User
from app.social.models import Course, UserCourse, PERSON_AGE_RANGE_CHOICES, PERSON_GENDER_CHOICES, PERSON_TYPE_CHOICES, PERSON_LEARNING_STYLE_CHOICES, PERSON_INTEREST_CHOICES, USER_COURSE_EXPERIENCE_CHOICES, USER_COURSE_LEVEL_CHOICES, USER_COURSE_YEARS_CHOICES, USER_COURSE_REASON_CHOICES, USER_COURSE_CREDIT_CHOICES, USER_COURSE_GOAL_CHOICES
import random

def random_choice(choice):
   return choice[random.randint(0,len(choice)-1)][0]

def random_availability():
   return '{0:048b}'.format(random.getrandbits(48))

courses = Course.objects.all()
i=0
for c in courses:
   print "%d: %s"%(i,c)
   i+=1

done = False
while not done:
   c = int(raw_input("Which course? "))
   print "%s"%courses[c]
   done = raw_input("Correct? (y/n) ") == "y"
num = int(raw_input("How many? "))
course = courses[c]

print "Generating"
for i in range(num):
   name = os.urandom(8).encode('hex')
   print "  %d: %s@test.com"%(i,name)

   user = User.objects.create_user(
       username = '%s@test.com'%name,
       password = name,
       email = '%s@test.com'%name
     )
   user.save()
   profile = user.get_profile()
   profile.age = random_choice(PERSON_AGE_RANGE_CHOICES)
   profile.gender = random_choice(PERSON_GENDER_CHOICES)
   profile.person_type = random_choice(PERSON_TYPE_CHOICES)
   profile.learning_style = random_choice(PERSON_LEARNING_STYLE_CHOICES)
   profile.interest = random_choice(PERSON_INTEREST_CHOICES)
   profile.monday_availability = random_availability()
   profile.tuesday_availability = random_availability()
   profile.wednesday_availability = random_availability()
   profile.thursday_availability = random_availability()
   profile.friday_availability = random_availability()
   profile.saturday_availability = random_availability()
   profile.sunday_availability = random_availability()
   profile.save()

   c = UserCourse()
   c.user = profile
   c.course = course
   c.general_experience = random_choice(USER_COURSE_EXPERIENCE_CHOICES)
   c.general_level = random_choice(USER_COURSE_LEVEL_CHOICES)
   c.topic_experience = random_choice(USER_COURSE_EXPERIENCE_CHOICES)
   c.topic_level = random_choice(USER_COURSE_LEVEL_CHOICES)
   c.years_experience = random_choice(USER_COURSE_YEARS_CHOICES)
   c.reason = random_choice(USER_COURSE_REASON_CHOICES)
   c.credit = random_choice(USER_COURSE_CREDIT_CHOICES)
   c.goals = random_choice(USER_COURSE_GOAL_CHOICES)
   c.save()

print "DONE"