from django.shortcuts import render
from .models import Product
from django.core.serializers.json import DjangoJSONEncoder
import json 

def products(request):
    context = {
        'title':'Products',
        'products':Product.objects.all()
    }
    return render(request,'product/index.html',context)

def cartview(request,ost):
    orderList = ost.split(',')
    products = Product.objects.filter(pk__in=orderList).values('id','name','price','image')
    product = json.dumps(list(products),cls=DjangoJSONEncoder)
    return render(request,'product/cartview.html',{'product':product});