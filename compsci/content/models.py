from django.db import models
from django.conf import settings
# Create your models here.

class HomePageTopPost(models.Model):
    title = models.TextField()
    message = models.TextField()
    create_at = models.DateTimeField(auto_now = True)
    upload = models.ImageField(upload_to ='uploads/')
    Bg_Colour = models.TextField()
