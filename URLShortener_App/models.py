from django.db import models

# Create your models here.



class URLShortener(models.Model):
    original_url = models.URLField()
    short_url = models.URLField()

    created_at = models.DateTimeField(auto_now_add=True)
