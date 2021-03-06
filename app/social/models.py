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
   ('f','Female'),
   ('o','Other')
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
   ('Arc','Archeology'),
   ('Arc','Architecture and Design'),
   ('Are','Area studies'),
   ('Bus','Business'),
   ('Che','Chemistry'),
   ('Com','Computer Sciences'),
   ('Cul','Cultural and Ethnic Studies'),
   ('Div','Divinity'),
   ('Ear','Earth Sciences'),
   ('Eco','Economics'),
   ('Edu','Education'),
   ('Eng','Engineering'),
   ('Env','Environmental Studies and Forestry'),
   ('Fam','Family and Consumer Science'),
   ('Gen','Gender and Sexuality Studies'),
   ('Geo','Geography'),
   ('Hea','Health Science'),
   ('His','History'),
   ('Hum','Human Physical Performance and Recreation'),
   ('Jou','Journalism, Media Studies and Communication'),
   ('Law','Law'),
   ('Lib','Library and Museum Studies'),
   ('Lif','Life Sciences'),
   ('Lin','Linguistics'),
   ('Lit','Literature'),
   ('Log','Logic'),
   ('Mat','Mathematics'),
   ('Mil','Military Sciences'),
   ('Per','Performing Arts'),
   ('Phi','Philosophy'),
   ('Phy','Physics'),
   ('Pol','Political Science'),
   ('Psy','Psychology'),
   ('Pub','Public Administration'),
   ('Rel','Religion'),
   ('Soc','Social Work'),
   ('Soc','Sociology'),
   ('Spa','Space Science'),
   ('Sta','Statistics'),
   ('Sys','Systems Science'),
   ('Tra','Transportation'),
   ('Vis','Visual Arts'),
   ('Oth','Other')
)

COURSE_SERVICE_CHOICES = (
   ('u','Udacity'),
   ('c','Coursera'),
   ('e','edX')
)

USER_COURSE_EXPERIENCE_CHOICES = (
   ('f','First Timer'),
   ('h','Hobbyist'),
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
   ('b','Background for a new class'),
   ('e','Recommended by a friend/teacher'),
   ('t','Taking with a friend'),
   ('q','Required for a different course'),
   ('o','Other')
)

USER_COURSE_CREDIT_CHOICES = (
   ('y','Yes'),
   ('n','No')
)

USER_COURSE_GOAL_CHOICES = (
   ('g','Get a new job'),
   ('e','Gain experience in this topic'),
   ('c','Curiosity about a topic'),
   ('o','Other')
)

CIRCLE_ACTION_TYPES = (
   ('j','User joined'),
   ('c','User says')
)



class Course(models.Model):
   name = models.CharField(max_length=255)
   service = models.CharField(max_length=1,choices=COURSE_SERVICE_CHOICES)
   course_id = models.CharField(max_length=64)
   professor = models.CharField(max_length=255)
   url = models.URLField()

   students = models.ManyToManyField(User,through='UserCourse')

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

   bio = models.CharField(max_length=140,verbose_name="Tell us a little about yourself, (140 characters remaining)")

def createUserProfile(sender, instance, **kwargs):
    """Create a UserProfile object each time a User is created ; and link it.
    """
    UserProfile.objects.get_or_create(user=instance)

post_save.connect(createUserProfile, sender=User)

class UserCourse(models.Model):
   user = models.ForeignKey(User)
   course = models.ForeignKey(Course)
   general_level = models.CharField(
      max_length=1,
      choices=USER_COURSE_LEVEL_CHOICES,
      verbose_name="What is your level for this course's general area of study?")
   topic_level = models.CharField(
      max_length=1,
      choices=USER_COURSE_LEVEL_CHOICES,
      verbose_name="What is your level for this course's specific topic?")
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
   requests = models.ManyToManyField(User,through='CircleRequest',related_name='circle_request')
   public = models.BooleanField(default=False)

   def __unicode__(self):
      people = map(lambda u: u.first_name, self.users.all())
      return '%s with %s'%(self.course,", ".join(people))

class CircleUser(models.Model):
   circle = models.ForeignKey(Circle)
   user = models.ForeignKey(User)
   video = models.BooleanField(default=False)
   last_video = models.DateTimeField(auto_now=True)
   created = models.DateTimeField(auto_now=True)

class CircleAction(models.Model):
   circle = models.ForeignKey(Circle)
   user = models.ForeignKey(User) 
   type = models.CharField(max_length=1,choices=CIRCLE_ACTION_TYPES)
   text = models.TextField(null=True)
   created = models.DateTimeField(auto_now=True)
def createUserJoinAction(sender, instance, **kwargs):
    """Create a user joined action when they join
    """
    action = CircleAction(circle=instance.circle,user=instance.user,type='j')
    action.save()
post_save.connect(createUserJoinAction, sender=CircleUser)

class CircleRequest(models.Model):
   circle = models.ForeignKey(Circle)
   owner = models.ForeignKey(User,related_name='circle_request_owner')
   confirmed = models.ManyToManyField(User,related_name='circle_request_confirmer')
   created = models.DateTimeField(auto_now=True)
   deleted = models.BooleanField(default=False)

class PartnerRequest(models.Model):
   course = models.ForeignKey(Course,related_name='+')
   owner = models.ForeignKey(User,related_name='partner_request_owner')
   user = models.ForeignKey(User,related_name='partner_request_user')
   created = models.DateTimeField(auto_now=True)
   deleted = models.BooleanField(default=False)

   def owner_usercourse(self):
      return self.owner.usercourse_set.get(course=self.course)

   def user_usercourse(self):
      return self.user.usercourse_set.get(course=self.course)

class PartnerSuggest(models.Model):
   course = models.ForeignKey(Course,related_name='+')
   owner = models.ForeignKey(User,related_name='partner_suggest_owner')
   user = models.ForeignKey(User,related_name='partner_suggest_user')
   created = models.DateTimeField(auto_now=True)
   deleted = models.BooleanField(default=False)

class CircleSuggest(models.Model):
   owner = models.ForeignKey(User,related_name='circle_suggest_owner')
   circle = models.ForeignKey(Circle,related_name='circle_suggest_circle')
   created = models.DateTimeField(auto_now=True)
   deleted = models.BooleanField(default=False)

