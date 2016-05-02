from django.test import TestCase, Client
from pxl_master.pxl.models import UserModel, PXLBoard
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

    def test_user_profile(self):
        """Test if user has a profile."""
        self.assertIsInstance(self.user.profile, UserModel)
