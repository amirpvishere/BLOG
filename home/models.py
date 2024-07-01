from django.db import models


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=40)
    subject = models.CharField(max_length=150)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.subject
