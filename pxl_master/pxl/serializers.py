from models import UserModel
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('username',
                  'email',
                  'pxlboard_1',
                  'pxlboard_2',
                  'pxlboard_3')
