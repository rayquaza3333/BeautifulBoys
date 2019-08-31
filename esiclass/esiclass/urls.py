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
from django.urls import path, include
from esiapp import views
import registration
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('registration/', include('registration.urls', namespace = 'registration')),
    path('esiadmin/', include('esiadmin.urls', namespace = 'esiadmin')),
    path('about/', views.EsiViews.as_view(template_name = 'esiapp/about.html'), name = 'about' ),
    path('business/', views.EsiViews.as_view(template_name = 'esiapp/business.html'), name = 'business' ),
    path('coming_soon/', views.EsiViews.as_view(template_name = 'esiapp/coming_soon.html'), name = 'coming_soon' ),
    path('communication/', views.EsiViews.as_view(template_name = 'esiapp/communication.html'), name = 'communication' ),
    path('contact/', views.EsiViews.as_view(template_name = 'esiapp/contact.html'), name = 'contact' ),
    path('course_details/', views.EsiViews.as_view(template_name = 'esiapp/course_details.html'), name = 'course_details' ),
    path('footer/', views.EsiViews.as_view(template_name = 'esiapp/footer.html'), name = 'footer' ),
    path('form/', views.EsiViews.as_view(template_name = 'esiapp/form.html'), name = 'form' ),
    path('header/', views.EsiViews.as_view(template_name = 'esiapp/header.html'), name = 'header' ),
    path('hocvien/', views.EsiViews.as_view(template_name = 'esiapp/hocvien.html'), name = 'hocvien' ),
    path('index/', views.EsiViews.as_view(template_name = 'esiapp/index.html'), name = 'index' ),
    path('language/', views.EsiViews.as_view(template_name = 'esiapp/language.html'), name = 'language' ),
    path('login/', views.EsiViews.as_view(template_name = 'esiapp/login.html'), name = 'login' ),
    path('', views.EsiViews.as_view(template_name = 'esiapp/index.html'), name = 'esiviews' ),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
