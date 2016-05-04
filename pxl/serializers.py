from pxl import models
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer1(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',
                  'email',
                  'password',
                  )


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',
                  'password',
                  )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserModel
        fields = ('username',
                  'email',
                  'password',
                  'pxlboard_1',
                  'pxlboard_2',
                  'pxlboard_3')


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PXLBoardModel
        fields = ('mlb',
                  'nfl',
                  'nhl',
                  'headlines',
                  'weather',
                  'owner',)
