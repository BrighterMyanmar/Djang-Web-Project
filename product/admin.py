from django.contrib import admin
from .models import Product, OrderItems, Orders

admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(OrderItems)
