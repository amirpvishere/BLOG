from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from post.models import Article, Category, Comment
from django.core.paginator import Paginator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


def post_details(request, slug):
    articles = Article.objects.get(slug=slug)
    if request.method == 'POST':
        body = request.POST.get('body')
        parent_id = request.POST.get('parent_id')
        Comment.objects.create(user=request.user, article=articles, body=body, parent_id=parent_id)
    return render(request, 'post/post-details.html', context={'articles': articles})


def blog_enteries(request):
    articles = Article.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 2)
    object_list = paginator.get_page(page_number)
    return render(request, 'post/article_list.html', context={'articles': object_list})


def category_sub(request, pk=None):
    category = get_object_or_404(Category, id=pk)
    articles = category.articles.all()
    return render(request, 'post/article_list.html', context={'articles': articles})


def search(request):
    q = request.GET.get('q')
    article = Article.objects.filter(title__icontains=q)
    page_number = request.GET.get('page')
    paginator = Paginator(article, 2)
    object_list = paginator.get_page(page_number)
    return render(request, 'post/article_list.html', context={'articles': object_list})


class ArticleListView(ListView):
    model = Article
    context_object_name = 'articles'
    paginate_by = 2


class ArticleCreateView(CreateView):
    model = Article
    fields = ('title', 'body','image')
    template_name = 'post/create_a_article.html'

    def get_success_url(self):
        return reverse_lazy('home:home')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.save()
        return super().form_valid(form)


class UpdateArticleView(UpdateView):
    model = Article
    fields = ('title', 'body', 'image')
    template_name = 'post/update_your_post.html'

    def get_success_url(self):
        return reverse_lazy('home:home')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.author = self.request.user
        instance.save()
        return super().form_valid(form)


class ArticleDeleteView(DeleteView):
    model = Article
    success_url = reverse_lazy('home:home')
    template_name = 'post/delete_post.html'





