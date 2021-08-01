from django.contrib import admin
from accounts.models import NewUser
# Register your models here.
from .models import *
admin.site.register(HomePageTopPost)
admin.site.register(GalleryImages)
admin.site.register(UserProfile)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Topic)
