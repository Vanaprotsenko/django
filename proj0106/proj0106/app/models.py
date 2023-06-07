from django.db import models


# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    year = models.CharField(max_length=255)
    madel = models.CharField(max_length=255)
    probeg = models.IntegerField()
    