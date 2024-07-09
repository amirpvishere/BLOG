from django.contrib.auth.models import User
from post.models import Article, Category


def user(request):
    user = User.objects.all()
    return {'user': user}


def sidebar(request):
    recent = Article.objects.order_by('-created_time')[:3]
    return {'recent': recent}


def categories(request):
    categories = Category.objects.all()
    return {'categories': categories}
