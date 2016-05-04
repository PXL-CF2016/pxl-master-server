from django.db import models
from django.conf import settings
from django.utils.encoding import python_2_unicode_compatible


class PXLBoardModel_1(models.Model):
    """PXL Board model."""

    mlb = models.BooleanField()
    nfl = models.BooleanField()
    nhl = models.BooleanField()
    headlines = models.BooleanField()
    weather = models.BooleanField()
    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=None,
    )


class PXLBoardModel_2(models.Model):
    """PXL Board model."""

    mlb = models.BooleanField()
    nfl = models.BooleanField()
    nhl = models.BooleanField()
    headlines = models.BooleanField()
    weather = models.BooleanField()
    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=None,
    )


class PXLBoardModel_3(models.Model):
    """PXL Board model."""

    mlb = models.BooleanField()
    nfl = models.BooleanField()
    nhl = models.BooleanField()
    headlines = models.BooleanField()
    weather = models.BooleanField()
    owner = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        default=None,
    )


@python_2_unicode_compatible
class UserModel(models.Model):
    """PXL User model."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )

    objects = models.Manager()
