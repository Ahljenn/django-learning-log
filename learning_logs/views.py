from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm

# Create your views here.
def index(request):
  """Home page for Learning Log app."""
  return render(request, 'learning_logs/index.html')

def topics(request):
  """Renders all topics in the learning log."""
  topics = Topic.objects.order_by('date_added')
  
  # Define a context to send to the template.
  # A context is a dictionary which the keys are names we'll use in the template to access the data.
  context = {'topics': topics}
  return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
  """Renders the single topic page and all its entries associated."""
  topic = Topic.objects.get(id=topic_id)
  entries = topic.entry_set.order_by('-date_added') # Minus sign sorts in reverse order.
  context = {
    'topic': topic,
    'entries': entries
  }
  return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
  """Renders the new topic page."""
  if request.method != 'POST':
    # No data is being submitted - create blank form.
    form = TopicForm()
  else:
    # Data is being submitted - process data.
    form = TopicForm(data=request.POST) # Create an instance of TopicForm and pass the user data.
    if form.is_valid():
      form.save() # Writes data from the form to database if form is valid.
      return redirect('learning_logs:topics') # Redirect user back to topics page after submitting form.
    
    
    #Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)