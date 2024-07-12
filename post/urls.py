from django.urls import path
from . import views


app_name = 'post'
urlpatterns = [
    path('details/<slug:slug>', views.post_details, name='details'),
    path('all', views.blog_enteries, name='all'),
    path("categories/<int:pk>", views.category_sub, name="categories"),
    path("search/", views.search, name="search"),
]

