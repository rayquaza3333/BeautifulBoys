"""esiclass URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from . import views

app_name = 'esiclass'

urlpatterns = [
    path('test/', views.TestView.as_view(), name = 'test'),
    path('about.html', views.EsiViews.as_view(template_name = 'esiclass/about.html'), name = 'about' ),
    path('business.html', views.EsiViews.as_view(template_name = 'esiclass/business.html'), name = 'business' ),
    path('coming_soon.html', views.EsiViews.as_view(template_name = 'esiclass/coming_soon.html'), name = 'coming_soon' ),
    path('communication.html', views.EsiViews.as_view(template_name = 'esiclass/communication.html'), name = 'communication' ),
    path('contact.html', views.EsiViews.as_view(template_name = 'esiclass/contact.html'), name = 'contact' ),
    path('course_details.html', views.EsiViews.as_view(template_name = 'esiclass/course_details.html'), name = 'course_details' ),
    path('footer.html', views.EsiViews.as_view(template_name = 'esiclass/footer.html'), name = 'footer' ),
    path('form.html', views.EsiViews.as_view(template_name = 'esiclass/form.html'), name = 'form' ),
    path('header.html', views.EsiViews.as_view(template_name = 'esiclass/header.html'), name = 'header' ),
    path('hocvien.html', views.EsiViews.as_view(template_name = 'esiclass/hocvien.html'), name = 'hocvien' ),
    path('index.html', views.EsiViews.as_view(template_name = 'esiclass/index.html'), name = 'index' ),
    path('language.html', views.EsiViews.as_view(template_name = 'esiclass/language.html'), name = 'language' ),
    path('login.html', views.EsiViews.as_view(template_name = 'esiclass/login.html'), name = 'login' ),
    path('', views.EsiViews.as_view(template_name = 'esiclass/index.html'), name = 'esiviews' ),
    path('admin/', admin.site.urls),
]
