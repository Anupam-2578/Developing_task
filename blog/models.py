from django.db import models

# Create your models here.
class Coderdata(models.Model):
    handle = models.CharField(max_length=100)
    rating = models.IntegerField()
    rank = models.CharField(max_length=50)