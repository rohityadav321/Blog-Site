from django.urls import path
from django.conf.urls import url
from . import views

appname = 'article'
urlpatterns = [
    # path('signup', views.signup, name="signup"),
    # path('login', views.login, name="login"),
    # path('logout', views.logout, name="logout"),
    # path('user_detail', views.user_detail, name="user"),
    path('', views.home, name="Blogg"),
    path('create_article', views.create, name="create"),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="article")


]
