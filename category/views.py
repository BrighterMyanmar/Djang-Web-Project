from django.shortcuts import render
from .models import Category, SubCategory
from .forms import SubCatFrom

def cats(request):
    context = {
        'title':"Categories",
        'cats':Category.objects.all()
    }
    return render(request,'category/cats.html',context)

def subs(request):
    cats = SubCategory.objects.all();
    return render(request,'category/subs.html',{'cats':cats})


def create(request):
    form = SubCatFrom()
    return render(request,'category/create.html',{'form':form})
