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

def ShowAddPasswordPage(request, oid):
    admin = Admin.objects.get(user_name = oid)
    forum = Forum.objects.all()   
    
    return render(request, "HTML/AddForumPassword.html", {'admin':admin,'forum':forum})  

def AddPasswordToForum(request, oid):
    user = Admin.objects.get(user_name = oid)

    passwo = request.POST.getlist('pass')

    Forums_Names = request.POST.getlist('item')
    Passwords = []

    for i in passwo:
        if i != '':
            Passwords.append(i)

    for i in list(range(len(Forums_Names))):
        name = Forums_Names[i]
        passw = Passwords[i]
        f = Forum.objects.get(Forum_name = name)
        f.password = passw
        f.save()


    forum = Forum.objects.all()  
    return render(request, "HTML/ForumAdmin.html", {'user':user,'forum':forum})  

def MoveToForumManagePage(request, oid):

    Pass = request.POST['password']
    ForumName = request.POST['select']

    user = User.objects.get(user_name = oid)
    forum = Forum.objects.get(Forum_name = ForumName)
    forumMessage = ForumMessage.objects.filter(Forum_name = ForumName)
    
    if forum.password == Pass and user.forum_manage == ForumName:
        Pictures = User.objects.all()
        return render(request, "HTML/ManagerForumPage.html", {'user':user,'forum':forum, 'forumMessage':forumMessage, 'Pictures':Pictures})  

    return HttpResponse("Bad!!")

def ShowUserForum(request, oid, foru):
    user = User.objects.get(user_name = oid)
    
    forum = Forum.objects.all()

    for i in forum:
        if foru in list(i.Forum_name.split()):
            foru = i.Forum_name


    forum = Forum.objects.get(Forum_name = foru)
    forumMessage = ForumMessage.objects.filter(Forum_name = foru)

    Pictures = User.objects.all()

    return render(request, "HTML/UserForumPage.html", {'user':user,'forum':forum, 'forumMessage':forumMessage , 'Pictures':Pictures})  


def UserPostAmessage(request, oid, foru):
    user = User.objects.get(user_name = oid)

    Sub = request.POST['name1']
    Mess = request.POST['name2']


    forum = Forum.objects.all()

    for i in forum:
        if foru in list(i.Forum_name.split()):
            foru = i.Forum_name
    forum = Forum.objects.get(Forum_name = foru)

    message= ForumMessage(Forum_name = foru,Author = oid ,subject=Sub, message=Mess )
    message.save()

    forumMessage = ForumMessage.objects.filter(Forum_name = foru)
    Pictures = User.objects.all()
    return render(request, "HTML/UserForumPage.html", {'user':user,'forum':forum, 'forumMessage':forumMessage, 'Pictures':Pictures})  

def UserMessageShowMessages(request, oid, Author, Subject):
    user = User.objects.get(user_name = oid)

    forumMessage = ForumMessage.objects.get(Author = Author, subject = Subject)

    comments = Comments.objects.filter(sender = Author, subject = Subject)
    Pictures = User.objects.all()
    return render(request, "HTML/UserMessagePage.html", {'user':user,'comments':comments, 'forumMessage':forumMessage, 'Pictures':Pictures})  


def AddCommentForMessage(request, oid, Author, Subject ):
    Mess = request.POST['name']
    
    user = User.objects.get(user_name = oid)

    forumMessage = ForumMessage.objects.get(Author = Author, subject = Subject)

    comm= Comments(sender = Author,subject = Subject ,Author=oid, message=Mess )
    comm.save()

    comments = Comments.objects.filter(sender = Author, subject = Subject)
    Pictures = User.objects.all()
    return render(request, "HTML/UserMessagePage.html", {'user':user,'comments':comments, 'forumMessage':forumMessage,  'Pictures':Pictures})  


def UserPostAmessageDelete(request, oid, foru):

    user = User.objects.get(user_name = oid)

    test = request.POST.getlist('item')

    forum = Forum.objects.all()

    for i in forum:
        if foru in list(i.Forum_name.split()):
            foru = i.Forum_name
    forum = Forum.objects.get(Forum_name = foru)

    for i in test:
        j = i.split()
        for k in Comments.objects.filter(sender = j[1], subject = j[0]):
            k.delete()
        a = ForumMessage.objects.get(subject = j[0] ,Author= j[1])
        a.delete()

    forumMessage = ForumMessage.objects.filter(Forum_name = foru)

    Pictures = User.objects.all()
    return render(request, "HTML/ManagerForumPage.html", {'user':user,'forum':forum, 'forumMessage':forumMessage , 'Pictures':Pictures})  

def ManageUserMessageShowMessages(request, oid, Author, Subject):
    user = User.objects.get(user_name = oid)

    forumMessage = ForumMessage.objects.get(Author = Author, subject = Subject)

    comments = Comments.objects.filter(sender = Author, subject = Subject)
    Pictures = User.objects.all()
    return render(request, "HTML/ManagerMessagePage.html", {'user':user,'comments':comments, 'forumMessage':forumMessage, 'Pictures':Pictures})  

def deleteMessageManyMessage(request, oid, Author, Subject ):
    user = User.objects.get(user_name = oid)

    test = request.POST.getlist('item')

    for i in test:
        j = i.split('papa1')
        k = Comments.objects.get(sender = j[1], subject = j[0], Author=j[2] ,message = j[3])
        k.delete()


    forumMessage = ForumMessage.objects.get(Author = Author, subject = Subject)

    comments = Comments.objects.filter(sender = Author, subject = Subject)
    Pictures = User.objects.all()
    return render(request, "HTML/ManagerMessagePage.html", {'user':user,'comments':comments, 'forumMessage':forumMessage,  'Pictures':Pictures})  


def Search(request, oid):
    username = request.POST['searchbar']

    if isExistsUser(username):
        admin = Admin.objects.get(user_name = oid)
        user = User.objects.filter(user_name = username)
        forum = Forum.objects.all()   
        return render(request, "HTML/UserManagement.html", {'admin':admin, 'user':user, 'forum':forum})  

    admin = Admin.objects.get(user_name = oid)
    user = User.objects.all()
    forum = Forum.objects.all()   
    
    return render(request, "HTML/UserManagement.html", {'admin':admin, 'user':user, 'forum':forum})  


def ManagerReport(request, oid):
    user = User.objects.get(user_name = oid)

    Pictures = User.objects.all()

    reports = Reports.objects.all()
    return render(request, "HTML/ManagerReportPage.html", {'user':user,'reports':reports, 'Pictures':Pictures})  