"""Admin configuration for the blog application."""

from django.contrib import admin

from blog.models import Post

admin.site.register(Post)
