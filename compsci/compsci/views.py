from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from content.models import HomePageTopPost, GalleryImage, Topic
from django.urls import path
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
class HomePage(ListView):
    template_name ="index.html"
    model = HomePageTopPost

    def get_context_data(self,*args, **kwargs):
         context = super(HomePage, self).get_context_data(*args,**kwargs)
         context['galleryimages_list'] = GalleryImage.objects.all()
         return context



# class student_login(LoginRequiredMixin,ListView):
#     login_url = 'login'
#     redirect_field_name = 'home'
#     context_object_name = 'topic_list'
#     model = Topic
#     page_kwarg = 'page'
#     template_name = 'student_home.html'

@login_required(login_url="/login/")
def student_login(request):
    topic = Topic.objects.all()
    units= topic.order_by().values_list('unit_name',flat = True).distinct() #find distinct() topic units to catorgise student_home page topics.
    context = {'topic':topic,'units':units}
    return render(request,'student_home.html', context)


@login_required(login_url="/login/")
def topicdetailview(request,pk):
    topic = Topic.objects.get(id = pk)
    list_quizes = topic.questionset_set.all()
    context ={'list_quizes':list_quizes,'topic':topic}
    return render(request,'topic_detail.html',context)
