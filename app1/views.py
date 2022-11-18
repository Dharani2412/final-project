from django.shortcuts import render
from .forms import Studentform,createUserForm
from .models import Student
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.

def register(request):
    if request.method == "POST":
        name=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']

        if password1==password2:
           user=User.objects.create_user(username=name,email=email,password=password1)
           user.save()
           messages.success(request,'your account has been created')
           return HttpResponseRedirect('/login')
        else:
            messages.warning(request,'password Mismatching...!!!')
            return HttpResponseRedirect('/register')
    else:
       form=createUserForm()
       return render(request,'register.html',{'form': form})



#def login(request):
 #   return render(request,"login.html")

def open(request):
    return render(request,"base.html")



def add_show(request):
    if request.method == "POST":
        fm=Studentform(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['first_name']
            lm=fm.cleaned_data['last_name']
            em=fm.cleaned_data['email']
            std=Student(first_name=nm,last_name=lm,email=em)
            std.save()
            return HttpResponseRedirect('/student')

    else:
        fm=Studentform()
    return render(request,'add_show.html',{'form': fm}) 

def table(request):
    fm=Student.objects.all()
    return render(request,'studenttable.html',{'fm': fm})

def delete(request, id):
    if request.method == "POST":
        di=Student.objects.get(pk=id)
        di.delete()
        return HttpResponseRedirect("/accounts/profile")

def update(request, id):
    if request.method == "POST":
        pi=Student.objects.get(pk=id)
        fm=Studentform(request.POST,instance=pi)
        if fm.is_valid():
           fm.save()
        return HttpResponseRedirect("/accounts/profile")

    else:
        pi=Student.objects.get(pk=id)
        fm=Studentform(instance=pi)
    return render(request,'show.html',{'form': fm})

def profile(request):
    fm=Student.objects.all()
    return render(request,'table.html',{'fm': fm})


def home(request):
    return render(request,'home.html')


    
    

