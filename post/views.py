from django.shortcuts import render
from post.models import Article


def post_details(request, pk):
    articles = Article.objects.get(id=pk)
    return render(request, 'post/post-details.html', context={'articles': articles})

