from django import forms
from django.contrib.auth.models import User
from massApp.models import UserProfile

class UserForm(forms.ModelForm):
    class Meta():
        model = User
        fields =['username', 'password', 'email']

class UserProfileForm(forms.ModelForm):
    class Meta():
        model = UserProfile
        fields = ['portfolio_site', 'profile_pic']
