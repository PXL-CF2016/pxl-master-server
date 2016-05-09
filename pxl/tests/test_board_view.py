from django.test import TestCase, Client
from pxl.models import PXLBoardModel
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
import factory
from rest_framework.test import APIRequestFactory
from mock import patch


class UserFactory(factory.django.DjangoModelFactory):
    """Set up a user."""
    class Meta:
        model = User
    username = factory.Faker('user_name')
    password = factory.Faker('password')


class BoardViewTests(TestCase):
    """Test board data API view."""

    def setUp(self):
        """Set up test client."""
        self.client = Client()
        self.user = UserFactory.create()

    @patch('pxl.views.generate_display')
    def test_board_view_post_request(self, generate_display):
        """Test board view post request."""
        mock_method = generate_display
        mock_method.return_value = ''
        token = Token.objects.get(user=self.user)
        params = {
            'token': token.key,
            'mlb': True,
            'nhl': True,
            'nfl': True,
            'headlines': True,
            'weather': True,
        }
        response = self.client.post('/api/v1.0/board_data/', params)
        board = PXLBoardModel.objects.get(owner=self.user)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['token'], token.key)
        self.assertEqual(board.mlb, True)
        self.assertEqual(board.nhl, True)
        self.assertEqual(board.nfl, True)
        self.assertEqual(board.headlines, True)
        self.assertEqual(board.weather, True)

    @patch('pxl.views.generate_display')
    def test_board_view_post_request_already_created(self, generate_display):
        """Test board view with an already created pxlboard."""
        mock_method = generate_display
        mock_method.return_value = ''
        token = Token.objects.get(user=self.user)
        params = {
            'mlb': '',
            'nhl': '',
            'nfl': '',
            'headlines': '',
            'weather': '',
        }
        new_board = PXLBoardModel(owner=self.user, **params)
        new_board.save()
        board_instance = PXLBoardModel.objects.get(owner=self.user)
        self.assertEqual(board_instance.mlb, False)
        self.assertEqual(board_instance.nfl, False)
        self.assertEqual(board_instance.nhl, False)
        self.assertEqual(board_instance.weather, False)
        self.assertEqual(board_instance.headlines, False)
        self.assertEqual(board_instance.owner, self.user)
        newparams = {
            'token': token.key,
            'mlb': 'true',
            'nhl': 'true',
            'nfl': 'true',
            'headlines': 'true',
            'weather': 'true',
        }
        response = self.client.post('/api/v1.0/board_data/', newparams)
        board = PXLBoardModel.objects.get(owner=self.user)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['token'], token.key)
        self.assertEqual(board.mlb, True)
        self.assertEqual(board.nhl, True)
        self.assertEqual(board.nfl, True)
        self.assertEqual(board.headlines, True)
        self.assertEqual(board.weather, True)
