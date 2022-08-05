from django.db import models

# Create your models here.
class Topic(models.Model):
  """A topic model that represents what the user is learning."""
  text = models.CharField(max_length=200)
  date_added = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    """Return a string representation of the topic model."""
    return self.text
  

class Entry(models.Model):
  """Something specific learned about the topic."""
  topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
  # ForeignKey is a reference to another record in the database
  # Connects each entry to a specifci topic - each having a key or ID when created
  # When a topic is deleted, all entries associated will be deleted too (cascading)

  text = models.TextField()
  date_added = models.DateTimeField(auto_now_add=True)

  class Meta:
    """Holds extra information for managing the model."""
    verbose_name_plural = 'entries'

  def __str__(self):
    """Return a string representation of the model.
       Shows only the first 50 characters of text.
    """
    return f"{self.text[:50]}..."