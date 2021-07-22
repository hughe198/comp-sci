from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.

class HomePageTopPost(models.Model):
    title = models.TextField()
    message = models.TextField()
    link = models.URLField(blank = True)
    create_at = models.DateTimeField(auto_now = True)
    upload = models.ImageField(upload_to ='static/content/', blank = False)
    Bg_Colour = models.TextField()

class GalleryImages(models.Model):
    image = models.ImageField(upload_to ='static/content/', blank = False)
    caption = models.TextField()


class BaseHelpers(models.Model):
    image = models.ImageField(upload_to ='static/question/', blank = True, null =True)
    class Meta:
        abstract = True


class Answer(BaseHelpers):
    question= models.ForeignKey(
        'Question',
        on_delete=models.CASCADE,
    )


class Topics(models.Model):
    topic_name = models.TextField()



class Question(BaseHelpers):
    topic= models.ForeignKey(
        'Topics',
        on_delete=models.CASCADE,
    )


class Tags(models.Model):
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        null =True, blank = True)
        
    tag = models.TextField(null = True,blank = True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
    image = models.ImageField(upload_to ='static/content/profiles', blank = False)

class User_Question_Answer(models.Model):
    user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        )
    answer= models.ForeignKey(Answer, on_delete = models.CASCADE)
