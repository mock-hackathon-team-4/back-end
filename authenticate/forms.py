from django import forms
from authenticate.models import UserProfileInfo, EventCreation
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password', 'email')


class UserProfileInfoForm(forms.ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')


class EventForm(forms.ModelForm):
    class Meta:
        model = EventCreation
        fields = ('name', 'description')
