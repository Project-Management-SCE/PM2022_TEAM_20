from django.urls import path
from WebIStudy.views import *
from django.urls import include, re_path

app_name = 'WebIStudy'

urlpatterns = [
    path('',HomePage, name='Login'),
    path('Register/',RegisterPage, name='Signup'), 
    path('Success/',ShowSuccess, name='Success'), 
    re_path(r'^Reg',Register, name='Register'), 
]