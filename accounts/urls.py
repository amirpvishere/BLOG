from django.urls import path
from . import views


urlpatterns = [
    path("", views.log_in),
    path("/register", views.register),
]