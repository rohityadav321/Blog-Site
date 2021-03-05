from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
import datetime
# from . import forms
from .models import Article
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.


def home(request):
    now = datetime.datetime.now()
    article = Article.objects.all().order_by('date')
    return render(request, 'index.html', {'years': now.year, 'article': article})


def article_detail(request, slug):
    now = datetime.datetime.now()
    article = Article.objects.get(slug=slug)
    return render(request, 'article.html', {'years': now.year, 'article': article})


@login_required(login_url="/accounts/login")
def create(request):
    return render(request, 'create.html')
