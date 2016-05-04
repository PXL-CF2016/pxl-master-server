from pxl import models
from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer1(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',
                  'password',
                  )


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',
                  'password',
                  )

class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PXLBoardModel
        fields = ('mlb',
                  'nfl',
                  'nhl',
                  'headlines',
                  'weather',
                  'owner',)
