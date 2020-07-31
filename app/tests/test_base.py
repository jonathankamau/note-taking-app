from django.test import Client, TestCase
from django.urls import reverse

class BaseTestClass(TestCase):

    def setUp(self):
        self.client = Client()
        fixtures = ['/app/data/categories.json',]

        user_registration_details = {'first_name': 'Jay',
                                    'last_name': 'Kline',
                                    'username': 'kline',
                                    'email': 'jay.kline@email.com',
                                    'password': 'jaykline2020'
                                }

        registration_wrong_creds = {'first_name': 'Jay',
                                    'last_name': 'Kline',
                                    'username': 'kline',
                                    'email': 'jay.kline',
                                    'password': 'j'
                                }
        user_login_details = {
            'username': 'kline',
            'password': 'jaykline2020'

        }


        self.register = self.client.post(
            reverse('register'), user_registration_details)
        
        
        self.reg_wrong_creds = self.client.post(
            reverse('register'), registration_wrong_creds)
        
        self.user_login = self.client.post(
            reverse('login'), user_login_details)
        

