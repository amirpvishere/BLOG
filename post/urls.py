from django.urls import path
from . import views


app_name = 'post'
urlpatterns = [
    path('details/<slug:slug>', views.post_details, name='details'),
    path('all', views.blog_enteries, name='all'),
]

