# Generated by Django 5.0.6 on 2024-07-09 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_alter_contactus_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='subject',
            field=models.CharField(blank=True, default='message', max_length=150),
        ),
    ]
