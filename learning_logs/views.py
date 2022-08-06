from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
  """Home page for Learning Log app."""
  return render(request, 'learning_logs/index.html')

@login_required # Decorator that checks if a user is logged in
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

@login_required
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

@login_required
def new_entry(request, topic_id):
  """Renders the new entry page for a topic."""
  topic = Topic.objects.get(id=topic_id)

  if request.method != 'POST':
    # No data is being submitted - create blank form.
    form = EntryForm()
  else:
    # Data is being submitted - process data.
    form = EntryForm(data=request.POST) # Create an instance of TopicForm and pass the user data.
    if form.is_valid():
      new_entry = form.save(commit=False) # Create a new try object and assign it to new_entry without saving to database.
      new_entry.topic = topic
      new_entry.save()
      return redirect('learning_logs:topic', topic_id=topic_id)
    
  # Display a blank or invalid form.
  context = {
    'topic': topic, 
    'form': form
  }
  return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
  """Renders the page to edit an existing entry."""
  entry = Entry.objects.get(id=entry_id)
  topic = entry.topic

  if request.method != 'POST':
    # Initial request; pre-fill form with current entry. For a GET request.
    form = EntryForm(instance=entry)
  else:
    # POST data submitted; process data.
    form = EntryForm(instance=entry, data=request.POST)
    if form.is_valid():
      form.save()
      return redirect('learning_logs:topic', topic_id=topic.id)
  
  context = {
    'entry': entry,
    'topic': topic,
    'form': form
  }

  return render(request, 'learning_logs/edit_entry.html', context)