from django.db import models
# from django.contrib.auth.models import User

class ForumPost(models.Model):
  """Forum post representing a post on a forum from a user."""
  # owner = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=225)
  text = models.TextField(max_length=2000)

  likes = models.PositiveIntegerField(default=0)
  dislikes = models.PositiveIntegerField(default=0)

  date_added = models.DateTimeField(auto_now_add=True)

  post_type = models.CharField(
    max_length=20,
    default="Discussion",
    choices=(
       ("Discussion", "Discussion"),
      ("Question", "Question"),
      ("Suggestion", "Suggestion"),
      ("Off-topic", "Off-topic"),
      ("Achievement", "Achievement"),
      ("Rant", "Rant"))
    )

  class Meta:
    verbose_name_plural = "Forum posts"

  def __str__(self):
    """Returns string representation of the forum post subject"""
    return self.title