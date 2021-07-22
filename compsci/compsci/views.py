from django.views.generic import TemplateView, ListView
from content.models import HomePageTopPost, GalleryImages
from django.urls import path

class HomePage(ListView):
    template_name ="index.html"
    model = HomePageTopPost

    def get_context_data(self,*args, **kwargs):
         context = super(HomePage, self).get_context_data(*args,**kwargs)
    #     context['HomePageTopPost'] = HomePageTopPost.objects.all()
         context['galleryimages_list'] = GalleryImages.objects.all()
         return context
