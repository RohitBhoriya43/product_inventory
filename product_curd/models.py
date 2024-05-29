from django.db import models

class Products(models.Model):
    name = models.CharField(max_length=100,null=True)
    category = models.CharField(max_length=255,null=True)
    price = models.FloatField(default=0.0)
