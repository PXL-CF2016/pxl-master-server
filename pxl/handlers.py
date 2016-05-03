from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from django.conf import settings
from pxl.models import UserModel
from rest_framework.authtoken.models import Token


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_profile(sender, instance, **kwargs):
#     if kwargs.get('created', False):
#         profile = UserModel(user=instance)
#         profile.save()
#
#
# @receiver(pre_delete, sender=settings.AUTH_USER_MODEL)
# def delete_profile(sender, instance, **kwargs):
#     instance.profile.delete()


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Token.objects.create(user=instance)
