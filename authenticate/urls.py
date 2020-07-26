# dappx/urls.py
from django.conf.urls import url
from django.urls import path

from authenticate import views

# SET THE NAMESPACE!
app_name = 'authenticate'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
    url(r'^create_event/$', views.create_event, name='create_event'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^event/$', views.create_event,name='event'),
]
