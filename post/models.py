from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title



class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    category = models.ManyToManyField(Category, related_name="articles")
    title = models.CharField(max_length=100)
    body = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/post')
    slug = models.SlugField(null=True, unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("post:details", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title
