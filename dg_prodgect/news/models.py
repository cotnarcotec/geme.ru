from django.db import models

class News(models.Model):
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=900)
    image = models.CharField(max_length=100)