"""Defines URL patterns for the users app."""

from django.urls import path, include

app_name = 'users'
urlpatterns = [
  # Default user auth urls
  path('', include('django.contrib.auth.urls')),
]