# Generated by Django 5.0.6 on 2024-07-21 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_alter_comment_article_alter_comment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='images/ArticleDefault.jpg', upload_to='images/post'),
        ),
    ]
