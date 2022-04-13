from django.contrib import admin
from django.urls import include, re_path
from django.urls import path , include


#from .models import Manager,Employee,Client


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('IStudy.urls')),
    path('accounts/', include('allauth.urls'))


]
