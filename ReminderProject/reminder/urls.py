from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sign_in', views.sign_in, name='sing_in'),
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('create_reminder', views.create_reminder, name='create_reminder'),
    path('out', views.exit_account, name='exit_account'),
]