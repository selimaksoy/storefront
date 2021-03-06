from __future__ import unicode_literals

from django.db import models

## That is for Category Class
class Category(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'

## That is for Product Class
class Product(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category)

    def __str__(self):
        return self.name
