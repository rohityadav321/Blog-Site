from django.urls import path
from . import views

appname = "accounts"

urlpatterns = [
    path(r'signup', views.signup, name="signup"),
    path(r'login', views.login, name="login"),
    path(r'logout', views.logout, name="logout"),
    # path('user_detail', views.user_detail, name="user"),
    # path('', views.home, name="codetopper")

]
