from django.urls import path 
from . import views

urlpatterns = [
    path('',views.products,name="all-product"),
    path('cartview/<str:ost>',views.cartview,name="cart-view"),
]