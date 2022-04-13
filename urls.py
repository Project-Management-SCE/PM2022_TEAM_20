from django.urls import path
from IStudy.views import *
from django.urls import include, re_path

app_name = 'IStudy'

urlpatterns = [
    path('',HomePage, name='Login'),
    path('Register/',RegisterPage, name='Signup'), 
    path('Success/',ShowSuccess, name='Success'), 
    re_path(r'Forums/(?P<oid>[-\w]*)',ShowForums, name='Forums'), 
    re_path(r'ChangeAccount/(?P<oid>[-\w]*)',ShowAccountInfo, name='ChangeDetails'), 
    re_path(r'AddInformation/(?P<oid>[-\w]*)',AddInformation, name='AddInformation'), 
    re_path(r'^Reg',Register, name='Register'), 
    re_path(r'^Log',Login, name='Log'), 
    re_path(r'^PassChanged/(?P<oid>[-\w]*)',ChangePassword, name='ChangePassword'), 
    re_path(r'^AddInfoChanged/(?P<oid>[-\w]*)',AddInformationToUser, name='AddDetails'), 
]
