from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('contact_us/list', views.contact_us_list, name='contact_us_list'),
]