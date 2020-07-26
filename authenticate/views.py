from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render
from authenticate.forms import UserForm, UserProfileInfoForm, EventForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import EventCreation

from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'authenticate/index.html')


def special(request):
    return HttpResponse("You are logged in !")


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request, 'authenticate/registration.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


def create_event(request):
    registered = False
    if request.method == 'POST':
        event_form = EventForm(data=request.POST)

        if event_form.is_valid():
            eve = event_form.save()
            eve.save()
            registered = True
        else:
            print(event_form.errors)
    else:
        event_form = EventForm();
    return render(request, 'authenticate/event.html',
                      {'event_form': event_form,
                   'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect("Already logged in")
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'authenticate/login.html', {})
