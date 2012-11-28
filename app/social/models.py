from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

PERSON_AGE_RANGE_CHOICES = (
   ('1','10-19'),
   ('2','20-29'),
   ('3','30-39'),
   ('4','40-49'),
   ('5','50-59'),
   ('6','60-69'),
   ('7','70-79'),
   ('8','80+')
)

PERSON_GENDER_CHOICES = (
   ('m','Male'),
   ('f','Female')
)

PERSON_TYPE_CHOICES = (
   ('h','Highschool Student'),
   ('u','Undergraduate Student'),
   ('g','Graduate Student'),
   ('a','Academic'),
   ('p','Professional'),
   ('o','Other')
)

PERSON_LEARNING_STYLE_CHOICES = (
   ('v','Visual'),
   ('a','Auditory'),
   ('t','Tactile')
)

PERSON_INTEREST_CHOICES = (
   ('Agr','Agriculture'),
   ('Ant','Anthropology'),
   ('Arc','Archaeology'),
   ('Arc','Architecture and Design'),
   ('Are','Area studies'),
   ('Bus','Business'),
   ('Che','Chemistry'),
   ('Com','Computer sciences'),
   ('Cul','Cultural and ethnic studies'),
   ('Div','Divinity'),
   ('Ear','Earth sciences'),
   ('Eco','Economics'),
   ('Edu','Education'),
   ('Eng','Engineering'),
   ('Env','Environmental studies and Forestry'),
   ('Fam','Family and consumer science'),
   ('Gen','Gender and sexuality studies'),
   ('Geo','Geography'),
   ('Hea','Health science'),
   ('His','History'),
   ('Hum','Human physical performance and recreation*'),
   ('Jou','Journalism, media studies and communication'),
   ('Law','Law'),
   ('Lib','Library and museum studies'),
   ('Lif','Life sciences'),
   ('Lin','Linguistics'),
   ('Lit','Literature'),
   ('Log','Logic'),
   ('Mat','Mathematics'),
   ('Mil','Military sciences'),
   ('Per','Performing arts'),
   ('Phi','Philosophy'),
   ('Phy','Physics'),
   ('Pol','Political science'),
   ('Psy','Psychology'),
   ('Pub','Public administration'),
   ('Rel','Religion'),
   ('Soc','Social work'),
   ('Soc','Sociology'),
   ('Spa','Space science'),
   ('Sta','Statistics'),
   ('Sys','Systems science'),
   ('Tra','Transportation'),
   ('Vis','Visual arts'),
   ('Oth','Other')
)

COURSE_SERVICE_CHOICES = (
   ('u','Udacity'),
   ('c','Coursera'),
   ('e','edX')
)

USER_COURSE_EXPERIENCE_CHOICES = (
   ('f','First Timer'),
   ('h','Hobbiest'),
   ('u','Undergraduate Student'),
   ('g','Graduate Student'),
   ('a','Academic'),
   ('p','Professional'),
   ('o','Other')
)

USER_COURSE_LEVEL_CHOICES = (
   ('n','Novice'),
   ('i','Intermediate'),
   ('e','Expert')
)

USER_COURSE_YEARS_CHOICES = (
   ('0','<1 year'),
   ('1','1-2 years'),
   ('2','2-5 years'),
   ('5','>5 years')
)

USER_COURSE_REASON_CHOICES = (
   ('n','Interest in new topic'),
   ('r','Refresher on topic'),
   ('o','Other')
)

USER_COURSE_CREDIT_CHOICES = (
   ('y','Yes'),
   ('n','No')
)

USER_COURSE_GOAL_CHOICES = (
   ('g','Get a new job'),
   ('e','Gain experience in this topic'),
   ('o','Other')
)


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
   age = models.CharField(
      max_length=1,
      choices=PERSON_AGE_RANGE_CHOICES,
      verbose_name="What is your age?")
   gender = models.CharField(
      max_length=1,
      choices=PERSON_GENDER_CHOICES,
      verbose_name="What is your gender?")
   person_type = models.CharField(
      max_length=1,
      choices=PERSON_TYPE_CHOICES,
      verbose_name="Which best describes you?")
   learning_style = models.CharField(
      max_length=1,
      choices=PERSON_LEARNING_STYLE_CHOICES,
      verbose_name="Which learning style best describes you?")
   interest = models.CharField(
      max_length=3,
      choices=PERSON_INTEREST_CHOICES,
      verbose_name="What is your area of interest?")
   monday_availability = models.CharField(max_length=48)
   tuesday_availability = models.CharField(max_length=48)
   wednesday_availability = models.CharField(max_length=48)
   thursday_availability = models.CharField(max_length=48)
   friday_availability = models.CharField(max_length=48)
   saturday_availability = models.CharField(max_length=48)
   sunday_availability = models.CharField(max_length=48)

   courses = models.ManyToManyField(Course,through='UserCourse')

def createUserProfile(sender, instance, **kwargs):
    """Create a UserProfile object each time a User is created ; and link it.
    """
    UserProfile.objects.get_or_create(user=instance)

post_save.connect(createUserProfile, sender=User)

class UserCourse(models.Model):
   user = models.ForeignKey(UserProfile)
   course = models.ForeignKey(Course)
   general_experience = models.CharField(
      max_length=1,
      choices=USER_COURSE_EXPERIENCE_CHOICES,
      verbose_name="What is your expertise in this general area?")
   general_level = models.CharField(
      max_length=1,
      choices=USER_COURSE_LEVEL_CHOICES,
      verbose_name="What is your level for this general area of study?")
   topic_experience = models.CharField(
      max_length=1,
      choices=USER_COURSE_EXPERIENCE_CHOICES,
      verbose_name="What is your expertise in this topic?")
   topic_level = models.CharField(
      max_length=1,
      choices=USER_COURSE_LEVEL_CHOICES,
      verbose_name="What is your level for this topic?")
   years_experience = models.CharField(
      max_length=1,
      choices=USER_COURSE_YEARS_CHOICES,
      verbose_name="How many years of experience do you have in this area?")
   reason = models.CharField(
      max_length=1,
      choices=USER_COURSE_REASON_CHOICES,
      verbose_name="Why are you taking this course?")
   credit = models.CharField(
      max_length=1,
      choices=USER_COURSE_CREDIT_CHOICES,
      verbose_name="Are you taking this course for credit at any academic institution?")
   goals = models.CharField(
      max_length=1,
      choices=USER_COURSE_GOAL_CHOICES,
      verbose_name="What is your primary goal from taking this course?")
   
   class Meta:
      unique_together = ("user", "course")

class Circle(models.Model):
   course = models.ForeignKey(Course)
   users = models.ManyToManyField(User,through='CircleUser')
   requests = models.ManyToManyField(User,through='CircleRequest',related_name='request')
   public = models.BooleanField(default=False)

class CircleUser(models.Model):
   circle = models.ForeignKey(Circle)
   user = models.ForeignKey(User)
   joined = models.DateTimeField(null=True)

class CircleRequest(models.Model):
   circle = models.ForeignKey(Circle)
   user = models.ForeignKey(User,related_name='requester')
   created = models.DateTimeField(auto_now=True)
   confirmed = models.ManyToManyField(User)

class CircleSuggestion(models.Model):
   course = models.ForeignKey(Course)
   users = models.ManyToManyField(User)
   confirmed = models.ManyToManyField(User,related_name='confirmer')
   deleted = models.BooleanField()