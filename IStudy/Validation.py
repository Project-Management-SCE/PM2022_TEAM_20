from models import *

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

