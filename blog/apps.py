"""Module for configuring the Blog app in a Django project."""

from django.apps import AppConfig


class BlogConfig(AppConfig):
    """Configuration class for the Blog app."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
