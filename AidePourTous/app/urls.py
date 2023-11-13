from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("home/", views.home, name="home"),
    path("base/", views.base, name="base"),
    path("accounts/", include("django.contrib.auth.urls")),
]