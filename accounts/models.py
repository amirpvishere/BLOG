from django.db import models


class Profile(models.Model):
    fullname = models.CharField(max_length =30)
    username = models.CharField(max_length =30)
    password = models.CharField(max_length =30)


