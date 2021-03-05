from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'BLogg'
urlpatterns = [
    url(r'^$', views.home, name="Blogg"),
    url(r'^create_article/$', views.create, name="create"),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name="article"),


]
