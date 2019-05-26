from django.db import models

class News(models.Model):
    title = models.CharField(max_length=300)
    text = models.CharField(max_length=3000)
    image = models.CharField(max_length=1000)