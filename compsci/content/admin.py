from django.contrib import admin

# Register your models here.
from .models import HomePageTopPost, GalleryImages

admin.site.register(HomePageTopPost)
admin.site.register(GalleryImages)
