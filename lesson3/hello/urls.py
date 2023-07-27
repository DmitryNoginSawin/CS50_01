from django.urls import path

from .import views

urlpatrerns = [
    path("", views.index, name="index")
]