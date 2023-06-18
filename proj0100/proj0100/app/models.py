from django.db import models


class Comp(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    size = models.IntegerField()
    image = models.ImageField(upload_to='comps/')
    
