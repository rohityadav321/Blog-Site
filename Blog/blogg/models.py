from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):

    title = models.CharField(max_length=252)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    # author=models.ForeignKey(User,Default = "null")

    def __str__(self):
        return self.title

    def short(self):
        return self.body[0:50]+"..."
