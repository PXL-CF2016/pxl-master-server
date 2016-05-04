
from django.test import TestCase, Client
from django.contrib.auth.models import User
from test_models import UserFactory
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from pxl.models import UserModel

class TestRegistration(APITestCase):
    """Test Class Registration API View."""

    def test_registration_view_no_get(self):
        """Expect get request not allowed for registration view."""
        response = self.client.get('/api/v1.0/registration/')
        self.assertEqual(response.status_code, 405)

    def test_create_account_201(self):
        """Test that user can register and user is added to the database."""
        response = self.client.post('/api/v1.0/registration/',
                                    {'email': 'test@test.com',
                                     'username': 'tester',
                                     'password': 'iluvtests123',
                                     }, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(UserModel.objects.count(), 1)

    def test_create_account_400(self):
        """Test that registration form is incomplete and user is not saved."""
        response = self.client.post('/api/v1.0/registration/',
                                    {'email': 'test@test.com',
                                     'username': 'blah',
                                     'password': '',
                                     }, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(UserModel.objects.count(), 0)

class TestLogin(APITestCase):
    """Test Class for Login API View."""

    def setUp(self):
        self.superuser = User.objects.create_superuser('bob', 'bob@bob.com', 'secretsecret')

    def login_view_get(self):
        """ Expect 200 status code for login view."""
        response = self.client.get('/api/v1.0/login/')
        self.assertEqual(response.status_code, 200)

    def test_valid_login(self):
        """Expect valid user login."""
        logged_in = self.client.post('/api/v1.0/login/', {'username': 'bob', 'password': 'secretsecret'}, format='json')
        pass
        # to do: get this view passing

    def test_invalid_login(self):
        """Expect invalid login failure."""
        logged_in = self.client.post('/api/v1.0/login/', {'username': 'bob', 'password': ''}, format='json')
        pass
        # to do: get this view passing
