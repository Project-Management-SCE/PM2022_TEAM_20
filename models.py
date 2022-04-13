from django.db import models

# Create your models here.
class Admin(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return f'user_name: {self.user_name}, password: {self.password}, email: {self.email}'
    
    class Meta:
        pass
        
class User(models.Model):
    user_name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    campus = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    study_year = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='uploads/')

    def __str__(self):
        return f'user_name: {self.user_name}, password: {self.password},email: {self.email}'
    
    class Meta:
        app_label = 'user'
        db_table = 'WebIStudy_user'
