from django.views.generic import TemplateView, ListView
from content.models import HomePageTopPost, GalleryImage, Topic
from django.urls import path
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
class HomePage(ListView):
    template_name ="index.html"
    model = HomePageTopPost

    def get_context_data(self,*args, **kwargs):
         context = super(HomePage, self).get_context_data(*args,**kwargs)
         context['galleryimages_list'] = GalleryImage.objects.all()
         return context



class student_login(LoginRequiredMixin,ListView):
    login_url = 'login'
    redirect_field_name = 'home'
    context_object_name = 'topic_list'
    model = Topic
    page_kwarg = 'page'
    template_name = 'student_home.html'
