from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .Validation import *
from .preproccessor import *

def HomePage(request):
    return render(request, "HTML/HomePage.html")

def AdminPage(request, oid):
    user = Admin.objects.get(user_name = oid)
    forum = Forum.objects.all()
    return render(request, "HTML/ForumAdmin.html", {'user':user, 'forum':forum})


def RegisterPage(request):
    return render(request, "HTML/Register.html")

def ShowSuccess(request):
    return render(request, "HTML/RegisterSuccess.html")

def ShowForums(request, oid):
    user = User.objects.filter(user_name = oid)

    if(user.exists() == False):
        str = "WebIStudy/static/Pictures/student.png"
        user= User(user_name = oid, picture = str)                                                
        user.save()


    block = Blocklist.objects.filter(user_name = oid)
    user = User.objects.get(user_name = oid)
    forum = Forum.objects.all()

    lst = []

    for i in block:
        lst.append(i.Forum_name)

    block = lst 

    return render(request, "HTML/ForumSelect.html" ,{'user':user , 'forum':forum, 'block':block})


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

    if Authenticate != 'User' and Authenticate != 'Admin':
        error = 'Please select Authentication!'
        return render(request, 'HTML/HomePage.html', {'error':error}) 

    if(Login_Exists(Authenticate,Usrname,passw) == False):
        if Authenticate == 'User':
            user = User.objects.get(user_name = Usrname,password = passw)
            forum = Forum.objects.all()

            block = Blocklist.objects.filter(user_name = Usrname)

            lst = []

            for i in block:
                lst.append(i.Forum_name)

            block = lst 

            if user.blocked == 'Blocked':
                error =  user.user_name + " you are blocked !"
                return render(request, 'HTML/HomePage.html', {'error':error})  

            return render(request, "HTML/ForumSelect.html" ,{'user':user , 'forum':forum, 'block':block})
        else:
            user = Admin.objects.get(user_name = Usrname,password = passw)
            forum = Forum.objects.all()
            return render(request, "HTML/ForumAdmin.html" ,{'user':user , 'forum':forum})

    else:
        return render(request, 'HTML/HomePage.html') 

def ChangePassword(request, oid):
    user = User.objects.get(user_name = oid)

    passw = request.POST['password']
    passwordconf = request.POST['passwordconf']
    
    if len(passw)== 0 or len(passwordconf) == 0:
        error = "No values entered!"
        return render(request, "HTML/ChangePassword.html" , {'user':user, 'error':error})   

    if (Check_Password(passw,passwordconf)):
        error = "Password not matched!"
        return render(request, "HTML/ChangePassword.html" , {'user':user, 'error':error})
    
    user.password = passw
    user.save()

    forum = Forum.objects.all()
    return render(request, "HTML/ForumSelect.html" , {'user':user, 'forum':forum})

def AddInformationToUser(request, oid):
    user = User.objects.get(user_name = oid)

    username =  user.user_name
    passw =  user.password
    emil = user.email
    Blocked = user.blocked
    mAnager = user.manager
    Forum_manage = user.forum_manage

    User_Study = request.POST['StudyPlace']
    User_degree = request.POST['Degree']
    StudyYear = request.POST['year']
    Photo = request.POST['myfile']

    str = "WebIStudy/static/Pictures/" + Photo

    user.delete()

    user = User(user_name = username, password = passw, email = emil, blocked = Blocked, manager = mAnager , forum_manage = Forum_manage, picture = str , campus = User_Study, degree = User_degree, study_year = StudyYear)

    user.save()

    forum = Forum.objects.all()
    return render(request, "HTML/ForumSelect.html" , {'user':user, 'forum':forum})

def ShowManageForums(request):
    forum = Forum.objects.all()
    user = Admin.objects.get(user_name ="Admin1234")
    return render(request, "HTML/ManageForums.html", {'forum':forum, 'user':user})

def ActionAddForums(request):
    name = request.POST['forumname']
    Photo = request.POST['myFile']
    user = Admin.objects.get(user_name ="Admin1234")

    if CheckForumExist(name):
        forum = Forum.objects.all()
        return render(request, "HTML/ManageForums.html", {'forum':forum, 'user':user})
    
    
    str = "WebIStudy/static/Pictures/" + Photo

    form= Forum(Forum_name =name , picture = str)
    form.save()
    
    forum = Forum.objects.all()

    return render(request, "HTML/ManageForums.html", {'forum':forum, 'user':user})

def ShowAdminChangePassword(request, oid):
    user = Admin.objects.get(user_name = oid)
    return render(request, "HTML/AdminChangePassword.html" , {'user':user})

def AdminChangedPassword(request, oid):
    user = Admin.objects.get(user_name = oid)
    Eml = user.email
    str = "WebIStudy/static/Pictures/20220426192432adminMoshiko.png"

    passw = request.POST['password']
    passwordconf = request.POST['passwordconf']

    if len(passw)== 0 or len(passwordconf) == 0:
        error = "No values entered!"
        return render(request, "HTML/AdminChangePassword.html" , {'user':user, 'error':error})   
    
    if (Check_Password(passw,passwordconf)):
        error = "password not matched!"
        return render(request, "HTML/AdminChangePassword.html" , {'user':user ,'error':error})
    
    user.delete()

    user = Admin(user_name = oid, password = passw, email =Eml, picture = str )
    user.password = passw
    user.save()

    forum = Forum.objects.all()
    return render(request, "HTML/ForumAdmin.html" , {'user':user, 'forum':forum})

def DeleteForums(request): 
    test = request.POST.getlist('item')
    user = Admin.objects.get(user_name = "Admin1234")
    for i in test:
        a = Forum.objects.get(Forum_name = i)
        a.delete()

    forum = Forum.objects.all()
    return render(request, "HTML/DeleteForumPage.html", {'forum':forum, 'user':user})
    
def ShowDeleteForums(request):
        forum = Forum.objects.all() 
        user = Admin.objects.get(user_name="Admin1234")      
        return render(request, "HTML/DeleteForumPage.html", {'forum':forum, 'user':user})

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

    if len(Forums_Names) == 0:
        admin = Admin.objects.get(user_name = oid)
        forum = Forum.objects.all()
        error = "No forum selected!"  
        return render(request, "HTML/AddForumPassword.html", {'admin':admin,'forum':forum, 'error':error})  


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

    if len(Sub.split()) > 1:
        Pictures = User.objects.all()
        forum = Forum.objects.all()
        for i in forum:
            if foru in list(i.Forum_name.split()):
                foru = i.Forum_name


        forum = Forum.objects.get(Forum_name = foru)
        forumMessage = ForumMessage.objects.filter(Forum_name = foru)

        error = "Subject must be only one word!"

        return render(request, "HTML/UserForumPage.html", {'user':user,'forum':forum, 'forumMessage':forumMessage , 'Pictures':Pictures, 'error':error})  

    forum = Forum.objects.all()

    if CheckMessage(Sub, Mess):
        for i in forum:
            if foru in list(i.Forum_name.split()):
                foru = i.Forum_name
        forum = Forum.objects.get(Forum_name = foru)
        forumMessage = ForumMessage.objects.filter(Forum_name = foru)
        Pictures = User.objects.all()
        return render(request, "HTML/UserForumPage.html", {'user':user,'forum':forum, 'forumMessage':forumMessage, 'Pictures':Pictures})  

    forum = Forum.objects.all()

    for i in forum:
        if foru in list(i.Forum_name.split()):
            foru = i.Forum_name
    forum = Forum.objects.get(Forum_name = foru)

    #message= ForumMessage(Forum_name = foru,Author = oid ,subject=Sub, message=Mess )
    message= ForumMessage(Forum_name = foru,Author = oid ,subject=Sub, message=Mess, email = user.email )
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

    #comm= Comments(sender = Author,subject = Subject ,Author=oid, message=Mess )

    euser = User.objects.get(user_name = oid)
    comm= Comments(sender = Author,subject = Subject ,Author=oid, message=Mess, email = euser.email )
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
        report = Reports.objects.filter(sender = j[1], subject = j[0], Author=j[2] ,message = j[3])

        if report.exists():
            report = Reports.objects.get(sender = j[1], subject = j[0], Author=j[2] ,message = j[3])
            report.delete()
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


def ForumManagerUsers(request, oid):
    admin = User.objects.get(user_name = oid)
    blocklist = Blocklist.objects.filter(Forum_name = admin.forum_manage)
    user = User.objects.all()

    lst = []

    for i in blocklist:
        lst.append(i.user_name)
    
    block = lst


    return render(request, "HTML/ForumMangerBlockingPage.html", {'admin':admin, 'user':user, 'block':block})



def Block_User(request, oid):
    Operation = request.POST['oper']
    test = request.POST.getlist('item')

    admin = User.objects.get(user_name = oid)

    if Operation == "Block User":
        for i in test:
            if not Blocklist.objects.filter(user_name = i , Forum_name = admin.forum_manage).exists():
                user= Blocklist(Forum_name = admin.forum_manage, user_name = i)
                user.save()
    
    else:
        for i in test:
            if Blocklist.objects.filter(user_name = i , Forum_name = admin.forum_manage).exists():
                a = Blocklist.objects.get(user_name = i , Forum_name = admin.forum_manage)
                a.delete()

    blocklist = Blocklist.objects.filter(Forum_name = admin.forum_manage)

    lst = []

    for i in blocklist:
        lst.append(i.user_name)
    
    block = lst
    user = User.objects.all()
    

    return render(request, "HTML/ForumMangerBlockingPage.html", {'admin':admin, 'user':user, 'block':block})


def SearchMessages(request, oid, foru):
    user = User.objects.get(user_name = oid)


    forum = Forum.objects.all()

    for i in forum:
        if foru in list(i.Forum_name.split()):
            foru = i.Forum_name
    
    forum = Forum.objects.get(Forum_name = foru)

    return render(request, "HTML/UserSearchMessage.html", {'user':user, 'forum':forum})

def ToSearch(request, oid, foru):
    sub = request.POST['subject']
    
    sub = Preprocessor(sub).split()

    user = User.objects.get(user_name = oid)
    forum = Forum.objects.all()

    for i in forum:
        if foru in list(i.Forum_name.split()):
            foru = i.Forum_name

    forum = Forum.objects.get(Forum_name = foru)

    forumMessage = ForumMessage.objects.filter(Forum_name = foru)


    lst = []

    for i in forumMessage:
        if i.subject in sub:
            lst.append(i)
    
    forumMessage = lst
    Pictures = User.objects.all()
    return render(request, "HTML/UserForumPage.html", {'user':user,'forum':forum, 'forumMessage':forumMessage , 'Pictures':Pictures})  


def AddingDesc(request, oid, foru):
    user = User.objects.get(user_name = oid)
    forum = Forum.objects.all()

    for i in forum:
        if foru in list(i.Forum_name.split()):
            foru = i.Forum_name

    forum = Forum.objects.get(Forum_name = foru)

    return render(request, "HTML/AddDescription.html", {'user':user,'forum':forum})  

def UpdatingDes(request, oid, foru):

    sub = request.POST['subject']
    
    user = User.objects.get(user_name = oid)
    forum = Forum.objects.all()

    for i in forum:
        if foru in list(i.Forum_name.split()):
            foru = i.Forum_name

    forum = Forum.objects.get(Forum_name = foru)

    forum.Description = sub
    forum.save()

    return render(request, "HTML/AddDescription.html", {'user':user,'forum':forum})  



def UserMessageReportMessages(request, oid, Author, Subject):
    user = User.objects.get(user_name = oid)

    forumMessage = ForumMessage.objects.get(Author = Author, subject = Subject)

    comments = Comments.objects.filter(sender = Author, subject = Subject)
    Pictures = User.objects.all()
    return render(request, "HTML/UserMessageReportPage.html", {'user':user,'comments':comments, 'forumMessage':forumMessage, 'Pictures':Pictures})  

def Report(request, oid, Author, Subject ):
    user = User.objects.get(user_name = oid)

    test = request.POST.getlist('item')

    for i in test:
        j = i.split('papa1')
        k = Reports(sender = j[1], subject = j[0], Author=j[2] ,message = j[3])
        mes = Comments.objects.get(sender = j[1], subject = j[0], Author=j[2] ,message = j[3])
        mes.report = 'True'
        mes.save()
        k.save()


    forumMessage = ForumMessage.objects.get(Author = Author, subject = Subject)

    comments = Comments.objects.filter(sender = Author, subject = Subject)
    Pictures = User.objects.all()
    return render(request, "HTML/UserMessagePage.html", {'user':user,'comments':comments, 'forumMessage':forumMessage,  'Pictures':Pictures})  

def ManagerReport(request, oid):
    user = User.objects.get(user_name = oid)

    Pictures = User.objects.all()

    reports = Reports.objects.all()
    return render(request, "HTML/ManagerReportPage.html", {'user':user,'reports':reports, 'Pictures':Pictures})  


def BackToForumManage(request, oid):
    user = Admin.objects.get(user_name = oid)

    forum = Forum.objects.all()

    return render(request, "HTML/ForumAdmin.html", {'user':user,'forum':forum})  
