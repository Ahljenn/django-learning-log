from django.db import models

# Create your models here.
class Topic(models.Model):
  """A topic model that represents what the user is learning"""
  text = models.CharField(max_length=200)
  date_added = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    """Return a string representation of the topic model"""
    return self.text