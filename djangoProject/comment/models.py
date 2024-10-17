from django.contrib.auth.models import User
from django.db import models


class Comment(models.Model):
    author = models.CharField(max_length=100)
    content = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
