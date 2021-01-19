from django.shortcuts import render,redirect
from .forms import UserRegisterFrom
from django.contrib import messages

def register(request):
    if request.method == "POST":
        form = UserRegisterFrom(request.POST)
        if form.is_valid() :
            form.save() 
            username = form.cleaned_data.get('username')
            messages.success(request,f'Register Successs Mr.{username}')
            return redirect('/cats/')
    else :
        form = UserRegisterFrom()

    return render(request,'user/register.html',{'form':form})