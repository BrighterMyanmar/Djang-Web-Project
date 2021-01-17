from django.shortcuts import render, redirect
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
    if request.method == "POST":
       form = SubCatFrom(request.POST,request.FILES)
       if form.is_valid():
           form.save() 
           return redirect('/cats/subs')
        
    else :
        print("Get Method")
        form = SubCatFrom()

    return render(request,'category/create.html',{'form':form})
