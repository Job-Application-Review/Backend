from django.db import models

# Create your models here.

STATUS = (
    ("P", "Pending"),
    ("A", "Accepted"),
    ("R", "Rejected"),
)


class Application(models.Model):

    name = models.CharField(null=True, blank=True, max_length=100)
    email = models.EmailField(null=True, blank=True, max_length=254)
    phone = models.BigIntegerField(null=True, blank=True)
    city = models.CharField(null=True, blank=True, max_length=200)
    linkedin = models.URLField(null=True, blank=True, max_length=200)
    webiste = models.URLField(null=True, blank=True, max_length=200)
    resume = models.FileField(upload_to=None, max_length=254, null=True, blank=True)
    reason = models.TextField(null=True, blank=True)
    status = models.CharField(
        max_length=20, choices=STATUS, default="P", null=True, blank=True
    )

    def __str__(self):
        return self.name
