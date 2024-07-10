from django.shortcuts import render, get_object_or_404
from post.models import Article, Category
from django.core.paginator import Paginator


def post_details(request, slug):
    articles = Article.objects.get(slug=slug)
    return render(request, 'post/post-details.html', context={'articles': articles})


def blog_enteries(request):
    articles = Article.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 2)
    object_list = paginator.get_page(page_number)
    return render(request, 'post/all_post.html', context={'articles': object_list})


def category_sub(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    articles = category.articles.all()
    return render(request, 'post/all_post.html', context={'articles': articles})
