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
from general import views

urlpatterns = [
    path('test/', views.TestView.as_view(), name = 'test'),
    path('about.html', views.EsiViews.as_view(template_name = 'about.html'), name = 'esiviews' ),
    path('business.html', views.EsiViews.as_view(template_name = 'business.html'), name = 'esiviews' ),
    path('coming_soon.html', views.EsiViews.as_view(template_name = 'coming_soon.html'), name = 'esiviews' ),
    path('communication.html', views.EsiViews.as_view(template_name = 'communication.html'), name = 'esiviews' ),
    path('contact.html', views.EsiViews.as_view(template_name = 'contact.html'), name = 'esiviews' ),
    path('course_details.html', views.EsiViews.as_view(template_name = 'course_details.html'), name = 'esiviews' ),
    path('footer.html', views.EsiViews.as_view(template_name = 'footer.html'), name = 'esiviews' ),
    path('form.html', views.EsiViews.as_view(template_name = 'form.html'), name = 'esiviews' ),
    path('header.html', views.EsiViews.as_view(template_name = 'header.html'), name = 'esiviews' ),
    path('hocvien.html', views.EsiViews.as_view(template_name = 'hocvien.html'), name = 'esiviews' ),
    path('index.html', views.EsiViews.as_view(template_name = 'index.html'), name = 'esiviews' ),
    path('language.html', views.EsiViews.as_view(template_name = 'language.html'), name = 'esiviews' ),
    path('login.html', views.EsiViews.as_view(template_name = 'login.html'), name = 'esiviews' ),
    path('', views.EsiViews.as_view(template_name = 'index.html'), name = 'esiviews' ),
    path('admin/', admin.site.urls),
]
