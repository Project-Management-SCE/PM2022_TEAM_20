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
        self.assertEquals(False,Validation.Check_Password(111111,111111))
        self.assertEquals(True,Validation.Check_Password(123456,1444467))
        
    
       
