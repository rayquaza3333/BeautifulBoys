from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Contact
# Create your views here.

class TestView(TemplateView):
    pass

def test(request):

    if request.method == 'POST':
        name = request.POST.get('tenhocvien')
        phone = request.POST.get('sdthocvien')
        email = request.POST.get('emailhocvien')

        if 'recording' in request.FILES:
            recording = request.FILES['recording']
            Contact.objects.get_or_create(name = name, phone = phone, email = email, recording = recording)
        else:
            Contact.objects.get_or_create(name = name, phone = phone, email = email)

    return render(request, 'registration/test.html')




# business.php
# coming_soon.php
# communication.p
# contact.php
# course_details.html
# footer.php
# form.php
# header.php
# hocvien.php
# index.php
# language.php
# login.php
# robots.txt
