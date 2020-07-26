from django.db import models
from django.contrib.auth.models import User
from django.db.models import OneToOneField


class UserProfileInfo(models.Model):
    user: OneToOneField = models.OneToOneField(User, on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username


# class EventCreation(models.Model):
#     name = models.CharField(max_length=100)
#     description = models.TextField()
#
#     def __str__(self):
#         return self.name


class Volunteer(models.Model):
    name = models.CharField(max_length=100)
    status= models.CharField(max_length=100)
    eventname= models.CharField(max_length=100)

    def __str__(self):
        return self.name
