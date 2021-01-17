from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()

class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField() 
    parent = models.ForeignKey(Category,on_delete=models.CASCADE)
