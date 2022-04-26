from django.urls import path
from WebIStudy.views import *
from django.urls import include, re_path
from django.conf import settings
from django.conf.urls.static import static
app_name = 'WebIStudy'

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
    path('Manage/',ShowManageForums, name='ManageForums'), 
    re_path(r'^AddForum',ActionAddForums, name='AddForums'),
    re_path(r'ChangeAdminPassword/(?P<oid>[-\w]*)',ShowAdminChangePassword, name='ChangeAdminPassword'),  
    re_path(r'ChangedAdminPassword/(?P<oid>[-\w]*)',AdminChangedPassword, name='ChangedAdminPassword'),  
    path('Delete/',ShowDeleteForums, name='DeletePage'), 
    re_path(r'DeletePages/',DeleteForums, name='DeleteForum'),  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)