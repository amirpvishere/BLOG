from django.urls import path
from . import views


app_name = 'post'
urlpatterns = [
    path('details/<int:pk>', views.post_details, name='details'),
]