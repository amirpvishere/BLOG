from django.urls import path
from . import views


urlpatterns = [
    path("login", views.log_in),
    path("logout", views.log_out),
    path("signup", views.sign_up),
]