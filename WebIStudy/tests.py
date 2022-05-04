from django.test import TestCase, LiveServerTestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from chromedriver_py import binary_path
from .models import *
from WebIStudy import views
from WebIStudy import Validation
import unittest

from selenium import webdriver
#from selenium.webdriver.common.keys import keys

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



    def test_CheckForumExist(self):
       self.assertFalse(False,views.CheckForumExist('Computer Arcithecture'))
       self.assertTrue(True,views.CheckForumExist('Computer Science'))
       self.assertTrue(True,views.CheckForumExist('Electrical Engineering'))
       self.assertTrue(True,views.CheckForumExist('Industrial Engineering and Management'))

    def test_Check_if_Forum_Manager(self):
        self.assertFalse(False,views.Check_if_Forum_Manager('Moshiko', 'Computer Science', '111211')) 
        self.assertTrue(True,views.Check_if_Forum_Manager('Moshiko', 'Computer Science', '111111')) 
        self.assertFalse(False,views.Check_if_Forum_Manager('Sergey', 'Electrical Engineering', '123441')) 



######################################### Integration tests ##########################################
#----------------------------------------------------------------------------------------------------#

class LoginTest(LiveServerTestCase):
    def testLoginUser(self):
        driver = webdriver.Chrome()
        driver.get('http://127.0.0.1:8000/')

        user_name = driver.find_element_by_name('username')
        password = driver.find_element_by_name('password')
        option = driver.find_element_by_name('Auth')

        user_name.send_keys('Moshiko')
        password.send_keys('111111')

        option.send_keys('User')
        submit = driver.find_element_by_name('submit')

        submit.click()

        assert 'iStudy - Forum Select' in driver.title

    def testLoginAdmin(self):
        driver = webdriver.Chrome()

        driver.get('http://127.0.0.1:8000/')

        user_name = driver.find_element_by_name('username')
        password = driver.find_element_by_name('password')
        option = driver.find_element_by_name('Auth')

        user_name.send_keys('Admin1234')
        password.send_keys('111111')

        option.send_keys('Admin')
        submit = driver.find_element_by_name('submit')

        submit.click()

        assert 'iStudy - Forum Select' in driver.title


class ManageForumTest(LiveServerTestCase):

    def testManageForum(self):
        driver = webdriver.Chrome()

        driver.get('http://127.0.0.1:8000/')

        user_name = driver.find_element_by_name('username')
        password = driver.find_element_by_name('password')
        option = driver.find_element_by_name('Auth')

        user_name.send_keys('Moshiko')
        password.send_keys('111111')

        option.send_keys('User')
        submit = driver.find_element_by_name('submit')

        submit.click()

        manage_button = driver.find_element_by_name('man_button')
        
        manage_button.click()


        forum = driver.find_element_by_name('select')
        password = driver.find_element_by_name('password')

        forum.send_keys('Computer Science')
        password.send_keys('111111')

        submit = driver.find_element_by_name('kaftor')

        submit.click()

        assert 'Manager Forum Page' in driver.title
