from django.test import TestCase
from models import *
from IStudy import views
from IStudy import Validation
import unittest

if __name__ == '__main__':
    unittest.main()
    
class URLTests(TestCase):
    #check urls of a local server pages 

    #check Register page
    def test_Register_Page(self):
        response = self.client.get('Register/')
        self.assertEqual(response.status_code, 404)
        

    #check General Register page
    def test_Success_Page(self):
        response = self.client.get('Success/')
        self.assertEqual(response.status_code, 404)
        
    #check Manager Register page
    def test_Reg_Page(self):
        response = self.client.get('Reg')
        self.assertEqual(response.status_code, 404)
        

class Views_Test(TestCase):
   
    #check Check_Password function
    def test_check_password(self):
        self.assertEquals(False,views.Check_Password(111111,111111))
        self.assertEquals(True,views.Check_Password(123456,1444467))
        
    
    # check isExistsClient function
    def test_User_is_exists(self):
        user = User(user_name = 'Sergey',password = '123456',email='Sergey@gmail.com')
        user.save()
        self.assertTrue(True,views.isExistsUser('Maor','Sergey@gmail.com'))
        self.assertFalse(False,views.isExistsUser('Vlad','Vlad@gmail.com'))
        
    
    # check Login_Exists function
    def test_Login(self):                                                                                                
       self.assertFalse(False,views.Login_Exists('User','Sergey','13456'))
       self.assertTrue(True,views.Login_Exists('User','Churkin','111111'))
       self.assertTrue(True,views.Login_Exists('Admin','Maor','123456'))
       self.assertFalse(False,views.Login_Exists('Admin','Vlad','13456'))
       
