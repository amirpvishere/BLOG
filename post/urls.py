from django.urls import path
from . import views


app_name = 'post'
urlpatterns = [
    path('details/<slug:slug>', views.post_details, name='details'),
    path('all', views.ArticleListView.as_view(), name='all'),
    path("categories/<int:pk>", views.category_sub, name="categories"),
    path("search/", views.search, name="search"),
    path('create', views.ArticleCreateView.as_view(), name='create_post'),
    path('update/<slug:slug>', views.UpdateArticleView.as_view(), name='update_post'),
    path('delete/<slug:slug>', views.ArticleDeleteView.as_view(), name='delete_post'),
]

