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

class UserProfile(models.Model):
    user = models.OneToOneField(User, null = True, on_delete = models.CASCADE)
    image = models.ImageField(upload_to ='static/content/profiles', blank = False)
