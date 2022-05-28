from django.test import TestCase, LiveServerTestCase, Client
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
#from chromedriver_py import binary_path
#import chromedriver_binary
from .models import *
from WebIStudy import views
from WebIStudy import Validation
import unittest
from selenium import webdriver

from django.urls import reverse
import json

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



class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.homepage_url = reverse('WebIStudy:Login')
        self.register_url = reverse('WebIStudy:Signup')
        self.Success_url = reverse('WebIStudy:Success')
        self.user_forum_url = reverse('WebIStudy:Forums' ,args=['Vlad'])
        self.ChangeDetails_url = reverse('WebIStudy:ChangeDetails',args=['Vlad'])
        self.AddInformation_url = reverse('WebIStudy:AddInformation',args=['Vlad'])
        self.Register_url = reverse('WebIStudy:Register')
        self.Log_url = reverse('WebIStudy:Log')
        self.ChangePassword_url = reverse('WebIStudy:ChangePassword', args=['Vlad'])
        self.AddDetails_url = reverse('WebIStudy:AddDetails', args=['Vlad'])
        self.ManageForums_url = reverse('WebIStudy:ManageForums')
        self.addForum_url = reverse('WebIStudy:AddForums')
        self.searching_url = reverse('WebIStudy:searching' , args=['Vlad', 'Computer Science'])
        self.ChangeAdminPassword_url = reverse('WebIStudy:ChangeAdminPassword' , args=['Gustavo'])
        self.ChangedAdminPassword_url = reverse('WebIStudy:ChangedAdminPassword' , args=['Gustavo'])

        User.objects.create(user_name = "Vlad", password="111111", email='Vlad@gmail.com', picture = "WebIStudy/static/Pictures/student.png")
        Admin.objects.create(user_name = "Gustavo", password="111111", email='Gustavo@gmail.com', picture = "WebIStudy/static/Pictures/student.png")
        Admin.objects.create(user_name = "Admin1234", password="111111", email='Admin1234@gmail.com', picture = "WebIStudy/static/Pictures/student.png")
        Forum.objects.create(Forum_name = "Computer Science", password="111111", Description='Description', picture = "WebIStudy/static/Pictures/student.png")



    def test_project_homepage_GET(self):
        response = self.client.get(self.homepage_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'HTML/HomePage.html')

    def test_project_register_GET(self):
        response = self.client.get(self.register_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'HTML/Register.html')

    def test_project_register_GET(self):
        response = self.client.get(self.register_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'HTML/Register.html')

    def test_project_success_GET(self):
        response = self.client.get(self.Success_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'HTML/RegisterSuccess.html')

    def test_project_user_forum_page_GET(self):
        response = self.client.get(self.user_forum_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'HTML/ForumSelect.html')

    def test_project_ChangeDetails_url_GET(self):
        response = self.client.get(self.ChangeDetails_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'HTML/ChangePassword.html')

    def test_project_AddInformation_url_GET(self):
        response = self.client.get(self.AddInformation_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'HTML/AddInformation.html')

    def test_project_Register_url_POST(self):
        response = self.client.post(self.Register_url, {
            'reg_username': 'SergeyGlot',
            'reg_password': '111111',
            'reg_password_conf': '111111',
            'reg_email': 'Sergey@gmail.com'
        })

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'HTML/HomePage.html')

    def test_project_Log_url_POST(self):
        response = self.client.post(self.Log_url, {
            'username': 'Vlad',
            'password': '111111',
            'Auth': 'User',
        })

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'HTML/ForumSelect.html')

    def test_project_LogAdmin_url_POST(self):
        response = self.client.post(self.Log_url, {
            'username': 'Gustavo',
            'password': '111111',
            'Auth': 'Admin',
        })

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'HTML/ForumAdmin.html')


    def test_project_ChangePassword_url_POST(self):
        response = self.client.post(self.ChangePassword_url, {
            'password': '111111',
            'passwordconf': '111111',
        })

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'HTML/ForumSelect.html')

    def test_project_AddDeTAILS_url_POST(self):
        response = self.client.post(self.AddDetails_url, {
            'StudyPlace': 'SCE',
            'Degree': 'Computer Science',
            'year': '3',
            'myfile': 'student.png'
        })

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'HTML/ForumSelect.html')
    
    def test_project_ManageForum_GET(self):
        response = self.client.get(self.ManageForums_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'HTML/ManageForums.html')


    def test_project_addForum_url_POST(self):
        response = self.client.post(self.addForum_url, {
            'forumname': 'Machine Engenerring',
            'myFile': 'books.JPG',
        })


        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'HTML/ManageForums.html')


    def test_project_search_url_POST(self):
        response = self.client.post(self.searching_url, {
            'subject': 'Jenkins Moshiko',
        })


        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'HTML/UserForumPage.html')
    
    
    def test_project_AdminPassword_GET(self):
        response = self.client.get(self.ChangeAdminPassword_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'HTML/AdminChangePassword.html')

    def test_project_AdminChanged_url_POST(self):
        response = self.client.post(self.ChangedAdminPassword_url, {
            'password': '111111',
            'passwordconf': '111111',
        })


        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'HTML/ForumAdmin.html')



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

    def test_CheckBlock(self):
        self.assertFalse(False,views.CheckBlock('Shimon'))
        self.assertFalse(False,views.CheckBlock('Moshiko'))

    def test_checkComment(self):
        self.assertTrue(True,views.checkComment('Shimon', 'Jenkins', 'Electrical'))



######################################### Integration tests ##########################################
#----------------------------------------------------------------------------------------------------#
'''
class LoginTest(LiveServerTestCase):
    def testLoginUser(self):
        driver = webdriver.Chrome("D:/onedrive/OneDrive - ac.sce.ac.il/Desktop/Alona/istudy/IStudyProject/IStudy/IStudy/WebIStudy/chromedriver.exe")
        driver.maximize_window()
        driver.get('http://127.0.0.1:8000/')

        user_name = driver.find_element_by_name('username')
        password = driver.find_element_by_name('password')
        option = driver.find_element_by_name('Auth')

        user_name.send_keys('Moshiko')
        password.send_keys('111111')

        option.send_keys('User')
        submit = driver.find_element_by_name('submit')

        submit.click()

        assert 'Forum Select' in driver.title

    def testLoginAdmin(self):
        driver = webdriver.Chrome("D:/onedrive/OneDrive - ac.sce.ac.il/Desktop/Alona/istudy/IStudyProject/IStudy/IStudy/WebIStudy/chromedriver.exe")
        driver.maximize_window()
        driver.get('http://127.0.0.1:8000/')

        user_name = driver.find_element_by_name('username')
        password = driver.find_element_by_name('password')
        option = driver.find_element_by_name('Auth')

        user_name.send_keys('Admin1234')
        password.send_keys('111111')

        option.send_keys('Admin')
        submit = driver.find_element_by_name('submit')

        submit.click()

        assert 'Forum Admin' in driver.title


    def testManageForum(self):
        driver = webdriver.Chrome("D:/onedrive/OneDrive - ac.sce.ac.il/Desktop/Alona/istudy/IStudyProject/IStudy/IStudy/WebIStudy/chromedriver.exe")
        driver.maximize_window()
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


    def testChangePassword(self):
        driver = webdriver.Chrome("D:/onedrive/OneDrive - ac.sce.ac.il/Desktop/Alona/istudy/IStudyProject/IStudy/IStudy/WebIStudy/chromedriver.exe")

        driver.maximize_window()
        driver.get('http://127.0.0.1:8000/')

        user_name = driver.find_element_by_name('username')
        password = driver.find_element_by_name('password')
        option = driver.find_element_by_name('Auth')

        user_name.send_keys('Moshiko')
        password.send_keys('111111')

        option.send_keys('User')
        submit = driver.find_element_by_name('submit')

        submit.click()

        menu = driver.find_element_by_name('user_botto')
        
        menu.click()


        changepassword = driver.find_element_by_name('changepass')
        changepassword.click()


        password = driver.find_element_by_name('password')
        confpass = driver.find_element_by_name('passwordconf')

        password.send_keys('111111')
        confpass.send_keys('111111')

        submit = driver.find_element_by_name('kaftor')

        submit.click()

        assert 'Forum Select' in driver.title


    def testAddMessage(self):
        driver = webdriver.Chrome("D:/onedrive/OneDrive - ac.sce.ac.il/Desktop/Alona/istudy/IStudyProject/IStudy/IStudy/WebIStudy/chromedriver.exe")
        driver.maximize_window()
        driver.get('http://127.0.0.1:8000/')

        user_name = driver.find_element_by_name('username')
        password = driver.find_element_by_name('password')
        option = driver.find_element_by_name('Auth')

        user_name.send_keys('Moshiko')
        password.send_keys('111111')

        option.send_keys('User')
        submit = driver.find_element_by_name('submit')

        submit.click()

        forum = driver.find_element_by_name('Computer Science')
        forum.click()


        newMessegeButton = driver.find_element_by_name('button')
        newMessegeButton.click()


        subject = driver.find_element_by_name('name1')
        messege = driver.find_element_by_name('name2')

        subject.send_keys('Docker')
        messege.send_keys('Please help me , i have problem!')

        submit = driver.find_element_by_name('kaftor')

        submit.click()

        assert 'User Forum Page' in driver.title
'''