# dappx/urls.py
from django.conf.urls import url
from django.urls import path

from authenticate import views

# SET THE NAMESPACE!
app_name = 'authenticate'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^user_login/insert/$', views.insert, name='insert'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    # url(r'^viewevents/$', views.showevents, name='showevents'),
]
