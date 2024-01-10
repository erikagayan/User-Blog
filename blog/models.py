"""Module defining the Post model for the blog application."""

from django.db import models

from users.models import User

MAX_TITLE_LENGTH = 255  # Constant for the maximum length of a post title


class Post(models.Model):
    """Represents a blog post."""

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=MAX_TITLE_LENGTH)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta(object):
        """Meta options for the Post model."""

        ordering = ['id']

    def __str__(self):
        """Return a string representation of the post title."""
        return self.title
