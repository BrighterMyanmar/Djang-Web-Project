from django.shortcuts import render,redirect
from .models import Product,Orders,OrderItems
from django.core.serializers.json import DjangoJSONEncoder
import json 
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

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

@login_required
def checkOut(request,ost):
    order = saveOrder(request,ost);
    saveOrderItem(request,order,ost);
    messages.success(request,f'Order Save Success!')
    return redirect('/')

def saveOrderItem(request,ordeObj,ost):
    orderList = ost.split(',');
    total = 0
    for order in orderList:
        proId = order.split(":")[0]
        proCount = order.split(":")[1]
        product = Product.objects.get(pk=proId)
        total += product.price * int(proCount)

        OrderItem = OrderItems() 
        OrderItem.name = product.name
        OrderItem.price = product.price
        OrderItem.image = product.image
        OrderItem.count = proCount
        OrderItem.orderId = ordeObj
        OrderItem.userId = request.user

        OrderItem.save()
    return True

def saveOrder(request,ost):
    orderList = ost.split(',');
    total = 0;
    for order in orderList:
        proId = order.split(":")[0]
        proCount = order.split(":")[1]
        product = Product.objects.get(pk=proId)
        total += product.price * int(proCount)
    
    order = Orders()
    order.count = len(orderList)
    order.total = total 
    order.userId = request.user

    order.save()
    return order;

def myOrder(request):
    user = request.user;
    orders = Orders.objects.filter(userId=user);
    odrs = []
    for order in orders:
        items = order.items.all();
        odrs.append({'order':order,'items':items})

    context = {
        "title":"My Orders",
        "orders":odrs
    }
    return render(request,'product/myorder.html',context)


