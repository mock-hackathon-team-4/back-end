from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from admindashboard.models import EventCreation

# Create your views here.
from admindashboard.forms import EventForm


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
    return render(request, 'admindashboard/event.html',
                  {'event_form': event_form,
                   'registered': registered})


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


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
        return HttpResponse("You are not admin")

def index(request):
    return render(request, 'admindashboard/index.html')

def showevents(request):
    events=EventCreation.objects.all()
    return render(request, 'admindashboard/show.html', {"events": events});