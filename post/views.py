from django.shortcuts import render,get_object_or_404
from post.models import Article


def post_details(request, slug):
    articles = get_object_or_404(Article, slug=slug)
    return render(request, 'post/post-details.html', context={'articles': articles})

