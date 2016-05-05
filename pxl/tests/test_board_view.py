from django.test import TestCase, Client
from pxl.models import PXLBoardModel
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
import factory
from rest_framework.test import APIRequestFactory

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

    def test_board_view_post_request(self):
        """Test board view post request."""
        token = Token.objects.get(user=self.user)
        params = {
            'token': token.key,
            'mlb': 'true',
            'nhl': 'false',
            'nfl': 'false',
            'headlines': 'true',
            'weather': 'true',
        }
        response = self.client.post('/api/v1.0/board_data/', params)
        board = PXLBoardModel.objects.get(owner=self.user)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['token'], token.key)
        self.assertEqual(board.mlb, True)
        self.assertEqual(board.nhl, False)
        self.assertEqual(board.nfl, False)
        self.assertEqual(board.headlines, True)
        self.assertEqual(board.weather, True)

    def test_board_view_post_request_already_created(self):
        """Test board view with an already created pxlboard."""
        token = Token.objects.get(user=self.user)
        params = {
            'token': token.key,
            'mlb': 'true',
            'nhl': 'false',
            'nfl': 'false',
            'headlines': 'true',
            'weather': 'true',
        }
        response = self.client.post('/api/v1.0/board_data/', params)
        newparams = {
            'token': token.key,
            'mlb': 'false',
            'nhl': 'true',
            'nfl': 'false',
            'headlines': 'true',
            'weather': 'true',
        }
        response = self.client.post('/api/v1.0/board_data/', newparams)
        board = PXLBoardModel.objects.get(owner=self.user)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['token'], token.key)
        self.assertEqual(board.mlb, False)
        self.assertEqual(board.nhl, True)
        self.assertEqual(board.nfl, False)
        self.assertEqual(board.headlines, True)
        self.assertEqual(board.weather, True)
