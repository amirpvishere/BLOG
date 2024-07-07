from django.shortcuts import render
from post.models import Article, Category
from home.models import ContactUs


def home(request):
    articles = Article.objects.all()
    recent_articles = Article.objects.all().order_by('created_time', 'updated_time')[:3]
    categories = Category.objects.all()
    return render(request, "home/index.html", {"articles": articles, "recent_articles": recent_articles, "categories": categories})


def contact_us(request):
    name = request.POST.get("name")
    subject = request.POST.get("subject")
    email = request.POST.get("email")
    message = request.POST.get("message")
    ContactUs.objects.create(name=name, email=email, subject=subject, message=message)
    return render(request, "home/contact.html")
