from django import forms
from authenticate.models import UserProfileInfo
from django.contrib.auth.models import User
from  authenticate.models import  Volunteer

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')


# class EventForm(forms.ModelForm):
#     class Meta:
#         model = EventCreation
#         fields = ('name', 'description')


class Volunteer(forms.ModelForm):
    name= forms.CharField(max_length=200)
    status= forms.CharField(max_length=200)
    eventname=forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = ('name', 'status', 'eventname')