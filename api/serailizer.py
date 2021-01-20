from rest_framework import serializers
from category.models import Category
from product.models import Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category 
        fields = ['id','name','image']

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = Product 
        fields = ['id','url','name','image','price','category']