from django.db import models

# Create your models here.

class Comp(models.Model):
    name = models.CharField(max_length=255)
    firm = models.CharField(max_length=255)
    year = models.IntegerField()
    size = models.IntegerField()
    price = models.IntegerField()
    
