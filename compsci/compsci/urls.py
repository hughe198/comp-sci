"""compsci URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import static, url
from django.conf import settings
from . import views
from accounts.views import registration_view, logout_view, login_view

urlpatterns = [
    path('', views.HomePage.as_view(), name="home"),
    path('admin/', admin.site.urls),
    path('register/',registration_view, name="register"),
    path('logout/', logout_view,name = "logout"),
    path('login/', login_view,name = "login"),
    path('topic_detail/<str:pk>/', views.topicdetailview, name="topic_detail"),
    path('student_home/', views.student_login, name ="student_home"),
    path('quiz/<str:pk>/', views.quiz, name='quiz')
]


urlpatterns += static.static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
