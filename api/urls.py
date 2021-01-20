from django.urls import path,include 
from rest_framework import routers 
from . import views

route = routers.DefaultRouter()
route.register('cats',views.CategoryView)
route.register('product',views.ProductView)

urlpatterns = [
    path('',include(route.urls))
]