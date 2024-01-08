import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "user_blog.settings")
django.setup()

import random
import json
from faker import Faker
from users.models import User
from blog.models import Post


with open("config.json", "r") as f:
    config = json.load(f)

bot = Faker()

for i in range(2):
    email = bot.email()
    username = email.split("@")[0]

    user = User.objects.create_user(username=username, email=email, password="password")

    title = bot.sentence()
    content = bot.text()

    post = Post.objects.create(author=user, title=title, content=content)
