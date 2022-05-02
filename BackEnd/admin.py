from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Admin)
admin.site.register(Forum)
admin.site.register(ForumMessage)
admin.site.register(Comments)
# Register your models here.
