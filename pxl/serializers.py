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


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserModel
        fields = ('username',
                  'email',
                  'password',
                  'pxlboard_1',
                  'pxlboard_2',
                  'pxlboard_3')


class BoardSerializer_1(serializers.ModelSerializer):
    class Meta:
        model = models.PXLBoardModel_1
        fields = ('mlb',
                  'nfl',
                  'nhl',
                  'headlines',
                  'weather')


class BoardSerializer_2(serializers.ModelSerializer):
    class Meta:
        model = models.PXLBoardModel_2
        fields = ('mlb',
                  'nfl',
                  'nhl',
                  'headlines',
                  'weather')


class BoardSerializer_3(serializers.ModelSerializer):
    class Meta:
        model = models.PXLBoardModel_3
        fields = ('mlb',
                  'nfl',
                  'nhl',
                  'headlines',
                  'weather')
