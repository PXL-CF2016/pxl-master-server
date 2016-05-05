
from django.test import TestCase, Client
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from mock import patch
import json

class TestRegistration(APITestCase):
    """Test Class Registration API View."""

    def test_registration_view_no_get(self):
        """Expect get request not allowed for registration view."""
        response = self.client.get('/api/v1.0/registration/')
        self.assertEqual(response.status_code, 405)

    @patch('pxl.views.return_credentials')
    def test_create_account_201(self, return_credentials):
        """Test that user can register and user is added to the database."""
        client = APIClient()
        mocked_function = return_credentials
        mocked_function.return_value = {'username': 'tester', 'password': 'iluvtests123'}
        response = client.post('/api/v1.0/registration/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), 1)

    @patch('pxl.views.return_credentials')
    def test_returned_token(self, return_credentials):
        """Test that user can register and user is added to the database."""
        client = APIClient()
        mocked_function = return_credentials
        mocked_function.return_value = {'username': 'tester', 'password': 'iluvtests123'}
        response = client.post('/api/v1.0/registration/')
        token_string = response.content.decode("utf-8")
        self.assertIn("token", token_string)

class TestLogin(APITestCase):
    """Test Class for Login API View."""

    def setUp(self):
        self.superuser = User.objects.create_superuser('bob', 'bob@bob.com', 'secretsecret')

    @patch('pxl.views.return_credentials')
    def test_valid_login(self, return_credentials):
        """Expect valid user login."""
        mocked_function = return_credentials
        mocked_function.return_value = {'username': 'bob', 'password': 'secretsecret'}
        logged_in = self.client.post('/api/v1.0/login/')
        self.assertEqual(logged_in.status_code, 200)

    @patch('pxl.views.return_credentials')
    def test_returned_token(self, return_credentials):
        """Expect token returned if login is successful."""
        mocked_function = return_credentials
        mocked_function.return_value = {'username': 'bob', 'password': 'secretsecret'}
        logged_in = self.client.post('/api/v1.0/login/')
        token_string = logged_in.content.decode("utf-8")
        self.assertIn("token", token_string)

    @patch('pxl.views.return_credentials')
    def test_bad_password(self, return_credentials):
        """Expect login failure if invalid password."""
        mocked_function = return_credentials
        mocked_function.return_value = {'username': 'bob', 'password': 'l33t49ck3r'}
        logged_in = self.client.post('/api/v1.0/login/')
        self.assertEqual(logged_in.status_code, 401)

    @patch('pxl.views.return_credentials')
    def test_bad_password_token(self, return_credentials):
        """Expect no token returned if password is incorrect."""
        mocked_function = return_credentials
        mocked_function.return_value = {'username': 'bob', 'password': 'l33t49ck3r'}
        logged_in = self.client.post('/api/v1.0/login/')
        token_string = logged_in.content.decode("utf-8")
        self.assertIn("Invalid username/password.", token_string)

    @patch('pxl.views.return_credentials')
    def test_no_password(self, return_credentials):
        """Expect login failure if password is empty."""
        mocked_function = return_credentials
        mocked_function.return_value = {'username': 'bob', 'password': ''}
        logged_in = self.client.post('/api/v1.0/login/')
        self.assertEqual(logged_in.status_code, 401)

    @patch('pxl.views.return_credentials')
    def test_no_password_token(self, return_credentials):
        """Expect no token returned if password field is empty."""
        mocked_function = return_credentials
        mocked_function.return_value = {'username': 'bob', 'password': ''}
        logged_in = self.client.post('/api/v1.0/login/')
        token_string = logged_in.content.decode("utf-8")
        self.assertIn("Invalid username/password.", token_string)

    @patch('pxl.views.return_credentials')
    def test_invalid_user(self, return_credentials):
        """Expect login failure for invalid user."""
        mocked_function = return_credentials
        mocked_function.return_value = {'username': '48ck3r', 'password': 'l33t12345'}
        logged_in = self.client.post('/api/v1.0/login/')
        self.assertEqual(logged_in.status_code, 401)

    @patch('pxl.views.return_credentials')
    def test_invalid_user_token(self, return_credentials):
        """Expect no token returned for invalid user login attempt."""
        mocked_function = return_credentials
        mocked_function.return_value = {'username': '48ck3r', 'password': 'l33t12345'}
        logged_in = self.client.post('/api/v1.0/login/')
        token_string = logged_in.content.decode("utf-8")
        self.assertIn("Invalid username/password.", token_string)
