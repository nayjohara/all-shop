from django.db import models

class Allshop(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField

