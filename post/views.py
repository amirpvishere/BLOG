from django.shortcuts import render, get_object_or_404
from post.models import Article, Category


def post_details(request, slug):
    articles = get_object_or_404(Article, slug=slug)
    return render(request, 'post/post-details.html', context={'articles': articles})


def blog_enteries(request):
    articles = Article.objects.all()
    return render(request, 'post/all_post.html', context={'articles': articles})


def category_sub(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    articles = category.articles.all()
    return render(request, 'post/all_post.html', context={'articles': articles})
