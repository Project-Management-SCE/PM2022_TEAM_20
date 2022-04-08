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

def ShowForums(request, oid):
    user = User.objects.get(user_name = oid)
    return render(request, "HTML/ForumSelect.html", {'user':user})

def ShowAccountInfo(request, oid):
    user = User.objects.get(user_name = oid)
    return render(request, "HTML/ChangePassword.html", {'user':user})

def AddInformation(request, oid):
    user = User.objects.get(user_name = oid)
    return render(request, "HTML/AddInformation.html", {'user':user})


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


def Login(request):
    Usrname = request.POST['username']
    passw = request.POST['password']
    Authenticate = request.POST['Auth']

    if(Login_Exists(Authenticate,Usrname,passw) == False):
        user = User.objects.get(user_name = Usrname,password = passw)
        return render(request, "HTML/ForumSelect.html" ,{'user':user})
    else:
        return render(request, 'HTML/HomePage.html') 

def ChangePassword(request, oid):
    user = User.objects.get(user_name = oid)

    passw = request.POST['password']
    passwordconf = request.POST['passwordconf']
    
    if (Check_Password(passw,passwordconf)):
        return render(request, "HTML/ChangePassword.html" , {'user':user})
    
    user.password = passw
    user.save()

    return render(request, "HTML/ForumSelect.html" , {'user':user})

def AddInformationToUser(request, oid):
    user = User.objects.get(user_name = oid)

    User_Study = request.POST['StudyPlace']
    User_degree = request.POST['Degree']
    StudyYear = request.POST['year']

    user.campus = User_Study
    user.degree = User_degree
    user.study_year = StudyYear
    user.save()

    return render(request, "HTML/ForumSelect.html" , {'user':user})