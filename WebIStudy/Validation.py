from .models import *

def isExistsUser(username, email2 = None):
    user = User.objects.filter(user_name = username)
    if  user.exists():
        return True

    user = User.objects.filter(email=email2)
    if  user.exists():
        return True

    return False

def Check_Password(password,conf_password):
    return not password == conf_password

def Login_Exists(user_type,username,passw):

    if user_type == 'Admin':
        user = Admin.objects.filter(user_name = username,password = passw)
        if not user.exists():
            return True

    if user_type == 'User':
        user = User.objects.filter(user_name = username,password = passw)
        if not user.exists():
            return True

    return False

def CheckForumExist(forumname):
    f = Forum.objects.filter(Forum_name = forumname)

    if f.exists():
        return True
    return False


def Check_if_Forum_Manager(oid, forumname, Pass):

    forum = Forum.objects.all()
    user = User.objects.all()

    for i in forum:
        if i.Forum_name == forumname:
            for j in user:
                if i.password == Pass and j.forum_manage == forumname:
                    return True

    return False

def CheckMessage(Sub, Mess):
    mess = ForumMessage.objects.filter(subject=Sub, message=Mess )

    if mess.exists():
        return True
    return False


def Check_if_all_space(passlist):
    for i in passlist:
        if i != '':
            return False
    return True

def CheckBlock(username):
    user = user = User.objects.all()

    for i in user:
        if i.user_name == username:
            if i.blocked == 'Blocked':
                return True
    return False

def checkComment(username, subject, forum):

    comment = ForumMessage.objects.all()

    for i in comment:
        if i.Forum_name == forum and i.Author == username and i.subject == subject:
            return True
    
    return False
