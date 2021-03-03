from django.urls import path
from . import views

urlpatterns = [
    # path('signup', views.signup, name="signup"),
    # path('login', views.login, name="login"),
    # path('logout', views.logout, name="logout"),
    # path('user_detail', views.user_detail, name="user"),
    path('', views.home, name="Blogg")

]
