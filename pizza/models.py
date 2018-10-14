from django.db import models

# Create your models here.


class Pizza(models.Model):
    name = models.TextField()
    price = models.IntegerField(blank=True)