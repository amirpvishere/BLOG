# Generated by Django 5.0.6 on 2024-07-09 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_alter_contactus_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='subject',
            field=models.CharField(default='message', max_length=150, null=True),
        ),
    ]
