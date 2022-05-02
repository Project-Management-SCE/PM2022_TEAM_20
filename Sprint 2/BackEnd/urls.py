from django.urls import path
from WebIStudy.views import *
from django.urls import include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

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
    re_path(r'UserManagementPage/(?P<oid>[-\w]*)',ShowUserManagePage, name='UsersManage'),  
    re_path(r'UserManagementApplied/(?P<oid>[-\w]*)',UserManageAction, name='UsersManageActions'),  
    re_path(r'AddPasswordPage/(?P<oid>[-\w]*)',ShowAddPasswordPage, name='AddPassword'),  
    re_path(r'PasswordAdded/(?P<oid>[-\w]*)',AddPasswordToForum, name='passwordAdded'), 
    re_path(r'ForumPage/(?P<oid>[-\w]*)',MoveToForumManagePage, name='ManageForum'), 
    re_path(r'UserSelectedForum/(?P<oid>[-\w]*)/(?P<foru>[-\w]*)',ShowUserForum, name='UserForum'), 
    re_path(r'UserPostAMessage/(?P<oid>[-\w]*)/(?P<foru>[-\w]*)',UserPostAmessage, name='Usermessage'),
    re_path(r'MessagesPageShow/(?P<oid>[-\w]*)/(?P<Author>[-\w]*)/(?P<Subject>[-\w]*)',UserMessageShowMessages, name='MessagesPage'),  
    re_path(r'MessagesAfterComments/(?P<oid>[-\w]*)/(?P<Author>[-\w]*)/(?P<Subject>[-\w]*)',AddCommentForMessage, name='MessagesCommentsPage'),  


    re_path(r'UserDeleteAMessage/(?P<oid>[-\w]*)/(?P<foru>[-\w]*)',UserPostAmessageDelete, name='UsermessageDelete'),
    re_path(r'CommanntPagesUserAdminPage/(?P<oid>[-\w]*)/(?P<Author>[-\w]*)/(?P<Subject>[-\w]*)',ManageUserMessageShowMessages, name='ManageMessagesPage'),  
    re_path(r'Messagedeletepagemanydeletemessages/(?P<oid>[-\w]*)/(?P<Author>[-\w]*)/(?P<Subject>[-\w]*)',deleteMessageManyMessage, name='DeleteMessageManyMessage'), 

    re_path(r'search/(?P<oid>[-\w]*)/',Search, name='searchuser'), 


    path('accounts/profile/',HomePage, name='testing'),

    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
