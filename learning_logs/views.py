from django.shortcuts import render
from .models import Topic

# Create your views here.
def index(request):
  """Home page for Learning Log app."""
  return render(request, 'learning_logs/index.html')

def topics(request):
  """Renders all topics in the learning log."""
  topics = Topic.objects.order_by('date_added')
  
  # Define a context to send to the template
  # A context is a dictionary which the keys are names we'll use in the template to access the data
  context = {'topics': topics}
  return render(request, 'learning_logs/topics.html', context)