from django.test import TestCase
from pxl.models import PXLBoardModel
from django.contrib.auth.models import User
import factory


class UserFactory(factory.django.DjangoModelFactory):
    """Set up a user."""
    class Meta:
        model = User
    username = factory.Faker('user_name')
    password = factory.Faker('password')


class HeadlineTests(TestCase):
    """Test sports API views."""

    def setUp(self):
        """Set up test user."""
        self.user = UserFactory()

    def test_pxlboard_model(self):
        """Test pxl board model."""
        params = {'mlb': 'true',
                  'nfl': '',
                  'nhl': '',
                  'headlines': '',
                  'weather': 'true'}
        newboard = PXLBoardModel(owner=self.user, **params)
        newboard.save()
        test_board = PXLBoardModel.objects.get(owner=self.user)
        self.assertEqual(test_board.owner, self.user)
        self.assertEqual(test_board.mlb, True)
        self.assertEqual(test_board.nfl, False)
        self.assertEqual(test_board.nhl, False)
        self.assertEqual(test_board.weather, True)
        self.assertEqual(test_board.headlines, False)
