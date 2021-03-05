from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
import datetime
# from . import forms
# from .models import Article
# Create your views here.


def logout(request):
    auth.logout(request)
    return redirect('/')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('/')
        else:
            messages.info(request, 'invalid username or password')
            return redirect('accounts:login')
    return render(request, 'login.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        conf_pass = request.POST['conf_pass']
        if len(password) < 8:

            messages.info(request, 'password too short')
            return redirect('accounts:signup')

        else:

            if password == conf_pass:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'user already taken')
                    return redirect('signup')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, 'email already taken')
                    return redirect('signup')
                else:
                    user = User.objects.create_user(
                        username=username, email=email, password=password)
                    user.save()
                    messages.info(request, 'account successfully created ')

                    return redirect('accounts:login')
            else:
                messages.info(request, 'password does not match')
                return redirect('accounts:signup')
    else:
        return render(request, 'signup.html')


# def user_detail(request):
#     now = datetime.datetime.now()
#     article = Article.objects.all().order_by('date')
#     return render(request, 'user.html', {'years': now.year, 'article': article})
