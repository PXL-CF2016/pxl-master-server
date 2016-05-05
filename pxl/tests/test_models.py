from django.test import TestCase, Client
from pxl.models import UserModel, PXLBoardModel_1
from pxl.models import PXLBoardModel_2, PXLBoardModel_3
from django.contrib.auth.models import User
import factory


class UserFactory(factory.django.DjangoModelFactory):
    """Set up a user factory."""
    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    password = factory.Faker('password')


class UserModelTest(TestCase):
    """Test user models."""

    def setUp(self):
        """Initialize a test user."""
        self.user = UserFactory.create()
        self.user.save()

    def test_user_profile(self):
        """Test if user has a profile."""
        self.assertIsInstance(self.user.profile, UserModel)
