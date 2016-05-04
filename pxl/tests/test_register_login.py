
from django.test import TestCase, Client
from django.contrib.auth.models import User
from test_models import UserFactory
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from pxl.models import UserModel

class TestRegistration(APITestCase):

    def test_create_account_201(self):
        response = self.client.post('/api/v1.0/registration/',
                                    {'email': 'test@test.com',
                                     'username': 'tester',
                                     'password': 'iluvtests123',
                                     }, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(UserModel.objects.count(), 1)

    def test_create_account_400(self):
        response = self.client.post('/api/v1.0/registration/',
                                    {'email': 'test@test.com',
                                     'username': 'blah',
                                     'passowrd': '',
                                     }, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(UserModel.objects.count(), 0)

class TestLogin(APITestCase):

    def test_invalid_user_login(self):
        self.cl = APIClient()
        response = self.cl.login(username="bleepblorp", password="secretsecret")
        self.assertEqual(response, False)

    def test_valid_user_login(self):
        self.cl = APIClient()
        user = UserFactory.create()
        user.save()
        response = self.cl.login(username=user.username, password=user.password)
        import pdb; pdb.set_trace()
        self.assertEqual(response, True)
