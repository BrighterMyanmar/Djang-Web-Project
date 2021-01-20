from django.shortcuts import render
from rest_framework import viewsets,permissions
from category.models import Category
from product.models import Product
from .customauth import IsAuth
from .serailizer import CategorySerializer, ProductSerializer

class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all() 
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated]
    http_method_names = ['get','post']

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]