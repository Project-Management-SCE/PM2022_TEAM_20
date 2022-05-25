from django.db import models
import datetime
import os
# Create your models here.

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = '%s%s' % (timeNow, old_filename)
    return os.path.join('WebIStudy/static/Pictures/', filename)



class Admin(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    picture = models.ImageField(upload_to=filepath,  null=True, blank=True)
    def __str__(self):
        return f'user_name: {self.user_name}, password: {self.password}, email: {self.email}'
    



class User(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    campus = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    study_year = models.CharField(max_length=50)
    picture = models.ImageField(upload_to=filepath,  null=True, blank=True)
    blocked = models.CharField(max_length=50, null=True)
    manager = models.CharField(max_length=50, null=True)
    forum_manage = models.CharField(max_length=50, null=True)


    def __str__(self):
        return f'user_name: {self.user_name}, password: {self.password},email: {self.email}'



class Forum(models.Model):
    Forum_name = models.CharField(max_length=300)
    Description = models.CharField(max_length=300)
    picture = models.ImageField(upload_to=filepath, null=True, blank=True)
    password = models.CharField(max_length=50, null=True)

    def __str__(self):
        return f'Forum_name: {self.Forum_name}, Description: {self.Description}'


class ForumMessage(models.Model):
    Forum_name = models.CharField(max_length=300)
    Author = models.CharField(max_length=50)
    subject = models.CharField(max_length=50)
    message = models.CharField(max_length=300)
    email = models.CharField(max_length=50,  null=True)

    def __str__(self):
        return f'Forum_name: {self.Forum_name}, Author: {self.Author}, Subject:{self.subject}, message:{self.message}'

class Comments(models.Model):
    sender = models.CharField(max_length=300)
    subject = models.CharField(max_length=50)
    Author = models.CharField(max_length=50)
    message = models.CharField(max_length=300)
    email = models.CharField(max_length=50,  null=True)
    report = models.CharField(max_length=50,  null=True)

    def __str__(self):
        return f'sender: {self.sender}, subject: {self.subject}, Author:{self.Author}, message:{self.message}'


class Blocklist(models.Model):
    Forum_name = models.CharField(max_length=300)
    user_name = models.CharField(max_length=50)

    def __str__(self):
        return f'Forum_name: {self.Forum_name}, user_name: {self.user_name}'


class Reports(models.Model):
    sender = models.CharField(max_length=300)
    subject = models.CharField(max_length=50)
    Author = models.CharField(max_length=50)
    message = models.CharField(max_length=300)


    def __str__(self):
        return f'sender: {self.sender}, subject: {self.subject}, Author:{self.Author}, message:{self.message}'