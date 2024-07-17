from django.urls import path
from . import views


app_name = 'accounts'

urlpatterns = [
    path("login", views.log_in, name="login"),
    path("logout", views.log_out, name="logout"),
    path("signup", views.sign_up, name="signup"),
    path("profile", views.edit_profile, name="profile"),
]