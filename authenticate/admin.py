from django.contrib import admin
from django.contrib import admin
from authenticate.models import UserProfileInfo, EventCreation
from authenticate.models import User
# Register your models here.
admin.site.register(UserProfileInfo)
admin.site.register(EventCreation)

