from django.views.generic import TemplateView, ListView
from content.models import HomePageTopPost
from django.urls import path

class HomePage(ListView):
    template_name ="index.html"
    model = HomePageTopPost
