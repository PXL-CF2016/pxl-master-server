from django.db import models
from django.conf import settings


class PXLBoard(models.Model):
    """PXL Board model."""

    mlb = models.BooleanField()
    nfl = models.BooleanField()
    nhl = models.BooleanField()
    headlines = models.BooleanField()
    weather = models.BooleanField()


class UserModel(models.Model):
    """PXL User model."""

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    pxlboard_1 = models.OneToOneField(PXLBoard)
    pxlboard_2 = models.OneToOneField(PXLBoard)
    pxlboard_3 = models.OneToOneField(PXLBoard)

    @property
    def is_active(self):
        return self.user.is_active
