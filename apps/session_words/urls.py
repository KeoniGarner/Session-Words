from django.urls import re_path
from . import views
urlpatterns=[
    re_path(r'^$', views.index),
    re_path(r'^add_word$', views.addWord),
    re_path(r'^clear$', views.clear),
]