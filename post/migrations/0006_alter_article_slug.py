# Generated by Django 5.0.6 on 2024-07-07 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_alter_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
