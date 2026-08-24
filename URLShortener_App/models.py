from django.db import models

# Create your models here.



class URLShortener(models.Model):
    url = models.URLField()
    short_url = models.URLField()
