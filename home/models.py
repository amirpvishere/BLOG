from django.db import models


class ContactUs(models.Model):
    name = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=40, null=True)
    subject = models.CharField(max_length=150, null=True)
    message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.subject
