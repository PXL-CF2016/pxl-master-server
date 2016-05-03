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


class PXLBoardModel_2(models.Model):
    """PXL Board model."""

    mlb = models.BooleanField()
    nfl = models.BooleanField()
    nhl = models.BooleanField()
    headlines = models.BooleanField()
    weather = models.BooleanField()


class PXLBoardModel_3(models.Model):
    """PXL Board model."""

    mlb = models.BooleanField()
    nfl = models.BooleanField()
    nhl = models.BooleanField()
    headlines = models.BooleanField()
    weather = models.BooleanField()


@python_2_unicode_compatible
class UserModel(models.Model):
    """PXL User model."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    pxlboard_1 = models.OneToOneField(PXLBoardModel_1)
    pxlboard_2 = models.OneToOneField(PXLBoardModel_2)
    pxlboard_3 = models.OneToOneField(PXLBoardModel_3)

    objects = models.Manager()
