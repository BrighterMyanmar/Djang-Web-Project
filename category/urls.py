from django.urls import path 
from .views import *

urlpatterns = [
    path('',cats,name="all-cats"),
    path('subs',subs,name="all-sub-cats"),
    path('subs/create',create,name="sub-create"),
    path('subs/<int:id>/delete',delete,name="sub-delete"),
    path('subs/<int:id>/edit',edit,name="sub-edit")
]