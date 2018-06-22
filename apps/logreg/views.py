from django.shortcuts import render,HttpResponse, redirect
from django.core import serializers
from django.http import JsonResponse
from django.contrib import messages
from .models import *
import json
import bcrypt

# Create your views here.

print("I M IN LOGREG VIEWS.PY")

def index(request):
    return render(request,'logreg/index.html')

def regProcess(request):
    errors = User.objects.basic_validator(request.POST)
    if (len(errors)):
        for key,value in errors.items():
            messages.error(request,value,extra_tags=key)
        return redirect('/')
    if User.objects.filter(email = request.POST['email']).count() > 0:
        print("This email is already registered!")
        messages.error(request,"This email is already registered!",extra_tags='email')
        return redirect('/')
    User.objects.create(first_name=request.POST['firstName'],
                        last_name = request.POST['lastName'],
                        email = request.POST['email'],
                        pwdhash = bcrypt.hashpw(request.POST['pwd'].encode(), bcrypt.gensalt()))
    messages.success(request,"Successfully registered!",extra_tags='registered')
    request.session['firstName'] = request.POST['firstName']
    return redirect('/success')

def valLogin(request):
    print(request.POST)
    user = User.objects.filter(email = request.POST['email'])
    if user.count() > 0 :
        if bcrypt.checkpw(request.POST['loginpwd'].encode(),user[0].pwdhash.encode()):
            request.session['firstName'] = user[0].first_name
            messages.success(request,"logged in Successfully!",extra_tags='login')
            return redirect('/success')
    messages.error(request,"Bad Credentials!",extra_tags='login')
    return redirect('/')

def success(request):
    return render(request,'logreg/success.html')

def logout(request):
    request.session.flush()
    return redirect('/')




# def new(request):
#     return render(request,'semirestfulusers/new.html')
#
# def create(request):
#     if request.method == "POST":
#         User.objects.create(first_name=request.POST['firstName'], last_name=request.POST['lastName'], email= request.POST['email'])
#         return redirect('/users')
#     else:
#         return redirect('/users')
#
# def show(request,number):
#     context={
#         'user': User.objects.get(id=number)
#     }
#     return render(request,'semirestfulusers/user.html',context)
#
# def edit(request,number):
#     context={
#         'user': User.objects.get(id=number)
#     }
#     return render(request,'semirestfulusers/edit.html',context)
