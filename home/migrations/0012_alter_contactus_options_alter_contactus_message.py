# Generated by Django 5.0.6 on 2024-07-09 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_alter_contactus_name_alter_contactus_subject'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactus',
            options={'verbose_name_plural': 'Contact Us'},
        ),
        migrations.AlterField(
            model_name='contactus',
            name='message',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
