from django.views.generic import TemplateView, ListView
from content.models import HomePageTopPost, GalleryImage
from django.urls import path

class HomePage(ListView):
    template_name ="index.html"
    model = HomePageTopPost

    def get_context_data(self,*args, **kwargs):
         context = super(HomePage, self).get_context_data(*args,**kwargs)
         context['galleryimages_list'] = GalleryImage.objects.all()
         return context

#class TeacherSignUp():
#    template_name ="teacher_signup.html"
