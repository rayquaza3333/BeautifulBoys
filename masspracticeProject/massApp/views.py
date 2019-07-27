from massApp.forms import UserForm, UserProfileForm

from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

# Index
def index(request):
    return render(request, 'massApp/index.html')

# Register

def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(request.POST, request.FILES)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit = False)
            profile.user = user
            profile.save()

            registered = True
        else:
            print(user.errors, profile.erros)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'massApp/register.html', {
                                                    'user_form': user_form,
                                                    "profile_form": profile_form,
                                                    "registered": registered,})

# login
def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username = username,password = password)

        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('massApp:special'))
            else:
                return HttpResponse('User is not active')
        else:
            print('Someone has tried to login')
            print('Username: {}'.format(username))
            print('Password: '.format(password))
    return render(request, 'massApp/login.html')

# logout
@login_required
def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

# special
@login_required
def special(request):
    return HttpResponse('You are login, nice')
