"""Defines URL patterns for the learning_logs app."""

from django.urls import path
from . import views #Imports the views.py module from the same directory as the current urls.py module.

app_name = "learning_logs"
urlpatterns = [
  path('', views.index, name='index'), #Home page
  #Arg 1. URL - Base URL here.
  #Arg 2. Specifies which function to call in views.py.
  #Arg 3. Provides the name for this URL pattern to be referred to in other code sections.
]