from django import forms
from .models import Topic

# ModelForm which uses the information from the models defined earlier to automatically build a form.
class TopicForm(forms.ModelForm):
  class Meta:
    """Nested Meta class to tell Django which model to base the form on and which fields to include."""
    model = Topic
    fields = ['text']
    labels = {'text': ''}