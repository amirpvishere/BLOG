from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from post.models import Article
from .forms import ContactUsForm
from .models import ContactUs
from django.views.generic import CreateView, UpdateView, DeleteView


def home(request):
    recent_articles = Article.objects.filter()
    articles = Article.objects.order_by('-created_time')[:3]
    return render(request, "home/index.html", context={"articles": articles, "recent_articles": recent_articles})


def contact_us_list(request):
    items = ContactUs.objects.all()
    return render(request, 'home/contact_us_list.html', context={"items": items})


def contact_us(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            ContactUs.objects.create(name=request.user.username, email=request.user.email, subject=subject, message=message)
            return redirect("home:contact_us")
    else:
        form = ContactUsForm()
    return render(request, "home/contact.html", {"form": form})




