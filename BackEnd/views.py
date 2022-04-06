from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .Validation import *

def HomePage(request):
    return render(request, "HTML/HomePage.html")

def RegisterPage(request):
    return render(request, "HTML/Register.html")

def ShowSuccess(request):
    return render(request, "HTML/RegisterSuccess.html")

def Register(request):
    username = request.POST['reg_username']
    passw = request.POST['reg_password']
    passwordconf = request.POST['reg_password_conf']
    email2 = request.POST['reg_email']

    if isExistsUser(username,email2):
        obj1="User already exist!"
        return render(request, "HTML/Register.html", {'obj1':obj1})

    if Check_Password(passw,passwordconf):
        obj1="Password not match!"
        return render(request, "HTML/Register.html" , {'obj1':obj1})



    user= User(user_name = username,password = passw ,email=email2)
    user.save()

    return render(request, 'HTML/HomePage.html')
