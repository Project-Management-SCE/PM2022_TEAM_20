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
    user = User.objects.filter(user_name = oid)

    if(user.exists() == False):
        str = "WebIStudy/static/Pictures/student.png"
        user= User(user_name = oid, picture = str)                                                ################### Google api ########################
        user.save()


    user = User.objects.get(user_name = oid)

    forum = Forum.objects.all()
    return render(request, "HTML/ForumSelect.html", {'user':user, 'forum':forum})

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

    str = "WebIStudy/static/Pictures/student.png"
    user= User(user_name = username,password = passw ,email=email2, picture= str)
    user.save()

    return render(request, 'HTML/HomePage.html')


def Login(request):
    Usrname = request.POST['username']
    passw = request.POST['password']
    Authenticate = request.POST['Auth']

    if(Login_Exists(Authenticate,Usrname,passw) == False):
        if Authenticate == 'User':
            user = User.objects.get(user_name = Usrname,password = passw)
            forum = Forum.objects.all()
            return render(request, "HTML/ForumSelect.html" ,{'user':user , 'forum':forum})
        else:
            user = Admin.objects.get(user_name = Usrname,password = passw)
            forum = Forum.objects.all()
            f = Forum.objects.get(Forum_name = 'Computer Science')
            return render(request, "HTML/ForumAdmin.html" ,{'user':user , 'forum':forum , 'f':f})

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

    forum = Forum.objects.all()
    return render(request, "HTML/ForumSelect.html" , {'user':user, 'forum':forum})

def AddInformationToUser(request, oid):
    user = User.objects.get(user_name = oid)

    User_Study = request.POST['StudyPlace']
    User_degree = request.POST['Degree']
    StudyYear = request.POST['year']
    Photo = request.POST['myfile']

    str = "WebIStudy/static/Pictures/" + Photo

    user.picture = str
    user.campus = User_Study
    user.degree = User_degree
    user.study_year = StudyYear
    user.save()

    forum = Forum.objects.all()
    return render(request, "HTML/ForumSelect.html" , {'user':user, 'forum':forum})

def ShowManageForums(request):
    forum = Forum.objects.all()
    return render(request, "HTML/ManageForums.html", {'forum':forum})

def ActionAddForums(request):
    name = request.POST['forumname']
    Photo = request.POST['myFile']
    
    if CheckForumExist(name):
        forum = Forum.objects.all()
        return render(request, "HTML/ManageForums.html", {'forum':forum})
    
    
    str = "WebIStudy/static/Pictures/" + Photo

    form= Forum(Forum_name =name , picture = str)
    form.save()
    
    forum = Forum.objects.all()

    return render(request, "HTML/ManageForums.html", {'forum':forum})

def ShowAdminChangePassword(request, oid):
    user = Admin.objects.get(user_name = oid)
    return render(request, "HTML/AdminChangePassword.html" , {'user':user})

def AdminChangedPassword(request, oid):
    user = Admin.objects.get(user_name = oid)

    passw = request.POST['password']
    passwordconf = request.POST['passwordconf']
    
    if (Check_Password(passw,passwordconf)):
        return render(request, "HTML/AdminChangePassword.html" , {'user':user})
    
    user.password = passw
    user.save()

    forum = Forum.objects.all()
    return render(request, "HTML/ForumAdmin.html" , {'user':user, 'forum':forum})

def DeleteForums(request): 
    test = request.POST.getlist('item')

    for i in test:
        a = Forum.objects.get(Forum_name = i)
        a.delete()

    forum = Forum.objects.all()
    return render(request, "HTML/DeleteForumPage.html", {'forum':forum})
    
def ShowDeleteForums(request):
        forum = Forum.objects.all()       
        return render(request, "HTML/DeleteForumPage.html", {'forum':forum})

def ShowUserManagePage(request, oid):
    admin = Admin.objects.get(user_name = oid)
    user = User.objects.all()
    forum = Forum.objects.all()   
    
    return render(request, "HTML/UserManagement.html", {'admin':admin, 'user':user, 'forum':forum})  

def UserManageAction(request, oid):
    Operation = request.POST['oper']
    ForumManage = request.POST['manage']
    
    test = request.POST.getlist('item')

    if Operation == "Assign as Manager":
        for i in test:
            a = User.objects.get(user_name = i)
            a.manager = 'Manager'
            a.forum_manage = ForumManage
            a.save()     
    
    elif Operation == "Block User":
        for i in test:
            a = User.objects.get(user_name = i)
            a.blocked = 'Blocked'
            a.save()


    elif Operation == "Release User":
        for i in test:
            a = User.objects.get(user_name = i)
            a.blocked = 'Not Blocked'
            a.save()

    forum = Forum.objects.all()   
    user = Admin.objects.get(user_name = oid)

    return render(request, "HTML/ForumAdmin.html", {'user':user,'forum':forum})  
















