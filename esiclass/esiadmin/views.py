from django.shortcuts import render
from django.views.generic import ListView, TemplateView

from registration.models import Contact
# Create your views here.

class ContactListView(ListView):
    model = Contact
    # def get_queryset(self):
    #     return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class TestView(TemplateView):
    pass
