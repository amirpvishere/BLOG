from django.urls import path
from . import views


urlpatterns = [
    path("", views.log_in),
    path("logout", views.log_out),
]