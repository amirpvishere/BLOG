from django.contrib import admin
from . import models


class CommentInlime(admin.TabularInline):
    model = models.Comment


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'show_image']
    list_filter = ['published']
    search_fields = ['title','body']
    inlines = [CommentInlime]


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['article', 'body', 'user']
    list_filter = ['user']


admin.site.register(models.Category)
admin.site.register(models.Like)
