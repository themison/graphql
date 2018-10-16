from django.db import models
from django.conf import settings    
from .helper import secret
# Create your models here.


class Pizza(models.Model):
    name = models.CharField(max_length=12)
    price = models.IntegerField()
    description = models.TextField(null=True)
    secretKey = models.CharField(max_length=10, editable=False)