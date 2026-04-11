from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    parent = None  # must be hierarchial to itself


class Brand(models.Model):
    name = models.CharField(max_length=100)


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
