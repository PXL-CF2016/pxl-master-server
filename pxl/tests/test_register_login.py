
from django.test import TestCase, Client
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework.test import APIRequestFactory
from mock import patch

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

    # @patch('pxl.views.return_credentials')
    # def test_create_account_400(self, return_credentials):
    #     """Test that registration form is incomplete and user is not saved."""
    #     client = APIClient()
    #     mocked_function = return_credentials
    #     mocked_function.return_value = {'username': 'bldkfjsdlkfj', 'password': ''}
    #     response = client.post('/api/v1.0/registration/')
    #     self.assertEqual(response.status_code, 400)
    #     self.assertEqual(User.objects.count(), 0)
    #     # this doesn't work rignt now


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
    def test_invalid_password(self, return_credentials):
        """Expect login failure if invalid password."""
        mocked_function = return_credentials
        mocked_function.return_value = {'username': 'bob', 'password': 'l33t49ck3r'}
        logged_in = self.client.post('/api/v1.0/login/')
        self.assertEqual(logged_in.status_code, 401)

    @patch('pxl.views.return_credentials')
    def test_no_password(self, return_credentials):
        """Expect login failure if password is empty."""
        mocked_function = return_credentials
        mocked_function.return_value = {'username': 'bob', 'password': ''}
        logged_in = self.client.post('/api/v1.0/login/')
        self.assertEqual(logged_in.status_code, 401)

    @patch('pxl.views.return_credentials')
    def test_invalid_user(self, return_credentials):
        """Expect login failure for invalid user."""
        mocked_function = return_credentials
        mocked_function.return_value = {'username': '48ck3r', 'password': 'l33t12345'}
        logged_in = self.client.post('/api/v1.0/login/')
        self.assertEqual(logged_in.status_code, 401)
