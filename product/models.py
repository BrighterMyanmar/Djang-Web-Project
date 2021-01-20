from django.db import models
from category.models import Category, SubCategory
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    price = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    subcat = models.ForeignKey(SubCategory,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Orders(models.Model):
    count = models.IntegerField()
    total = models.IntegerField()
    userId = models.ForeignKey(User,on_delete=models.CASCADE)

class OrderItems(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.CharField(max_length=100)
    count = models.IntegerField() 
    orderId = models.ForeignKey(Orders,on_delete=models.CASCADE,related_name='items')
    userId = models.ForeignKey(User,on_delete=models.CASCADE)