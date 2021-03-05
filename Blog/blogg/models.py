from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):

    title = models.CharField(max_length=252)
    body = models.TextField()
    slug = models.SlugField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def short(self):
        return self.body[:50]+"..."
