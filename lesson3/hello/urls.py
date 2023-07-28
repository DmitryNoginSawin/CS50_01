from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("dmitry", views.dmitry, name="Dmitry"),
    path("david", views.david, name="David")
]