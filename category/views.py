from django.shortcuts import render, redirect
from .models import Category, SubCategory
from .forms import SubCatFrom
from django.contrib.auth.decorators import login_required
from .decorators import allow_users

def cats(request):
    context = {
        'title':"Categories",
        'cats':Category.objects.all()
    }
    return render(request,'category/cats.html',context)

def subs(request):
    cats = SubCategory.objects.all();
    return render(request,'category/subs.html',{'cats':cats})

@login_required
@allow_users(allowed_roles=['admins'])
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

def delete(request,id):
    subcat = SubCategory.objects.get(pk=id)
    subcat.delete()
    return redirect('/cats/subs')

def edit(request,id):
    category = SubCategory.objects.get(pk=id)

    if request.method == "POST":
        form = SubCatFrom(request.POST,request.FILES,instance=category)
        if form.is_valid():
            form.save() 
            return redirect('/cats/subs')
    else :
        form = SubCatFrom(instance=category)
    
    return render(request,'category/edit.html',{'form':form})