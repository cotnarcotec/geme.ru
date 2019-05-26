from django.db import models
class Game(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=900)
    image = models.CharField(max_length=100)
