from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("hello", views.hello, name="hello"),
    path("error", views.error, name="error"),
    path("<str:title>", views.title, name="title")
]
