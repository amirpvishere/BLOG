from django.shortcuts import render
from post.models import Article
from home.models import ContactUs


def home(request):
    articles = Article.objects.all()
    return render(request, "home/index.html", {"articles": articles})


def contact_us(request):
    name = request.POST.get("name")
    subject = request.POST.get("subject")
    email = request.POST.get("email")
    message = request.POST.get("message")
    ContactUs.objects.create(name=name, email=email, subject=subject, message=message)
    return render(request, "home/contact.html")
