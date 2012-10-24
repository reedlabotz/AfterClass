from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

PERSON_TYPE_CHOICES = (('h','Highschool Student'),('u','Undergraduate Student'),('g','Graduate Student'),('p','Professional'),('r','Retired'),('o','Other'))

COURSE_SERVICE_CHOICES = (('u','Udacity'),('c','Coursera'),('e','edX'))

EXPERT_LEVEL_CHOICES = (('f','First Timer'),('h','Hobbiest'),('u','Undergraduate Student'),('g','Graduate Student'),('p','Professional'),('o','Other'))

EXPERT_TIME_CHOICES = (('0','<1 year'),('1','1-2 years'),('2','2-5 years'),('5','>5 years'))

NOVICE_INTERMEDIATE_EXPERT = (('n','Novice'),('i','Intermediate'),('e','Expert'))

REASON_CHOICES = (('n','Interest in new topic'),('r','Refresher on topic'),('o','Other'))


class Course(models.Model):
   name = models.CharField(max_length=255)
   service = models.CharField(max_length=1,choices=COURSE_SERVICE_CHOICES)
   course_id = models.CharField(max_length=64)
   professor = models.CharField(max_length=255)
   url = models.URLField()

   def __unicode__(self):
      return '%s: %s'%(self.get_service_display(),self.name)

   class Meta:
      ordering = ['service', 'name']

class UserProfile(models.Model):
   user = models.OneToOneField(User, primary_key=True)
   person_type = models.CharField(max_length=1,choices=PERSON_TYPE_CHOICES,verbose_name="What best describes you")
   courses = models.ManyToManyField(Course,through='UserCourse')
   monday_availability = models.CharField(max_length=32)
   tuesday_availability = models.CharField(max_length=32)
   wednesday_availability = models.CharField(max_length=32)
   thursday_availability = models.CharField(max_length=32)
   friday_availability = models.CharField(max_length=32)
   saturday_availability = models.CharField(max_length=32)
   sunday_availability = models.CharField(max_length=32)

def createUserProfile(sender, instance, **kwargs):
    """Create a UserProfile object each time a User is created ; and link it.
    """
    UserProfile.objects.get_or_create(user=instance)

post_save.connect(createUserProfile, sender=User)

class UserCourse(models.Model):
   user = models.ForeignKey(UserProfile)
   course = models.ForeignKey(Course)
   expert_level = models.CharField(max_length=1,choices=EXPERT_LEVEL_CHOICES,verbose_name="What is your expertise in the area")
   expert_time = models.CharField(max_length=1,choices=EXPERT_TIME_CHOICES,verbose_name="How long have you worked in this area")
   general_level = models.CharField(max_length=1,choices=NOVICE_INTERMEDIATE_EXPERT,verbose_name="What is your level in this general area")
   specific_level = models.CharField(max_length=1,choices=NOVICE_INTERMEDIATE_EXPERT,verbose_name="What is your level in this specific area")
   reason = models.CharField(max_length=1,choices=REASON_CHOICES,verbose_name="Why are you taking this course")

   class Meta:
      unique_together = ("user", "course")
   
