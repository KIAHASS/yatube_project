# group/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('<slug:slug>/', views.group_posts),
]