from django import forms
from .models import Topic, Entry

# ModelForm which uses the information from the models defined earlier to automatically build a form.
class TopicForm(forms.ModelForm):
  """Allow users to enter a new topic."""
  class Meta:
    """Nested Meta class to tell Django which model to base the form on and which fields to include."""
    model = Topic
    fields = ['text']
    labels = {'text': ''}

class EntryForm(forms.ModelForm):
  """Allow user to enter a new entry."""
  class Meta:
    model = Entry
    fields = ['text']
    labels = {'text': 'Entry:'}
    widgets = {'text': forms.Textarea(attrs={'cols':80})}
    # A widget is an HTML from element, such as a singe-lien text box, multi-line text area, or drop-down list.
