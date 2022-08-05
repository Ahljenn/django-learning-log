"""Defines URL patterns for the learning_logs app."""

from django.urls import path
from . import views 
#Imports the views.py module from the same directory as the current urls.py module.

app_name = 'learning_logs'
#Arg 1. URL / Path
#Arg 2. Specifies which function to call in views.py.
#Arg 3. Provides the name for this URL pattern to be referred to in other code sections.
urlpatterns = [
  
  # Home page
  path('', views.index, name='index'), #Home page

  # Page for all topics.
  path('topics/', views.topics, name='topics'),
  
  # Detail page for a single topic.
  path('topics/<int:topic_id>/', views.topic, name='topic'),

  #Page for adding a new topic
  path('new_topic/', views.new_topic, name='new_topic'),

]