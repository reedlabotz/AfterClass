from django.db import models
from django.contrib.auth.models import User

PERSON_TYPE_CHOICES = (('h','Highschool Student'),('u','Undergraduate Student'),('g','Graduate Student'),('p','Professional'),('r','Retired'),('o','Other'))

COURSE_SERVICE_CHOICES = (('u','Udacity'),('c','Coursera'),('e','edX'))

EXPERT_LEVEL_CHOICES = (('p','Professional'),('u','Undergraduate Student'),('g','Graduate Student'),('h','Hobbiest'),('f','First Timer'),('o','Other'))

EXPERT_TIME_CHOICES = (('0','<1'),('1','1-2'),('2','2-5'),('5','>5'))

NOVICE_INTERMEDIATE_EXPERT = (('n','Novice'),('i','Intermediate'),('e','expert_level'))

REASON_CHOICES = (('n','Interest in new topic'),('r','Refresher on topic'),('o','Other'))

class Person(User):
   person_type = models.CharField(max_length=1,choices=PERSON_TYPE_CHOICES)
   courses = models.ManyToManyField(Course,through=PersonCourses)


class Course(models.Model):
   name = models.CharField(max_length=255)
   service = models.CharField(max_length=1,choices=COURSE_SERVICE_CHOICES)
   course_id = models.CharField(max_length=64)
   url = models.UrlField()


class PersonCourses(models.Model):
   person = models.ForeignKey(Person)
   course = models.ForeignKey(Course)
   expert_level = models.CharField(max_length=1,choices=EXPERT_LEVEL_CHOICES)
   expert_time = models.CharField(max_length=1,choices=EXPERT_TIME_CHOICES)
   general_level = models.CharField(max_length=1,choices=NOVICE_INTERMEDIATE_EXPERT)
   specific_level = models.CharField(max_length=1,choices=NOVICE_INTERMEDIATE_EXPERT)
   reason = models.CharField(max_length=1,choices=REASON_CHOICES)
   
