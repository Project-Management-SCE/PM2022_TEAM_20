from django.contrib import admin
from django.urls import include, re_path
from django.urls import path , include

from django.urls import path
from WebIStudy.views import *
from django.urls import include, re_path
from django.conf import settings
from django.conf.urls.static import static

#from .models import Manager,Employee,Client


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('WebIStudy.urls')),
    path('accounts/', include('allauth.urls'))


]


