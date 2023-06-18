from django.db import models

# Create your models here.

from django.db import models

# Create your models here.
class Movies(models.Model):
   file = models.FileField(upload_to='documents/')
   image = models.ImageField(upload_to='images/')