from pxl import models
from pxl import serializers
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User


class LoginView(APIView):
    """Registration and login view."""

    def get(self, request, format=None):
        """Return user and authorization to front end."""
        content = {
            'user': unicode(request.user),
            'auth': unicode(request.auth)
        }
        return Response(content)

    def post(self, request, format=None):
        """Set username and password to database."""
        new_user = User
        new_user.username = request.username
        new_user.password = request.password
        new_user.email = request.email
        new_user.save()
        content = {
            'user': unicode(request.user),
            'auth': unicode(request.auth)
        }
        return Response(content)


class UserList(generics.ListCreateAPIView, generics.UpdateAPIView):
    serializer_class = serializers.UserSerializer
    queryset = models.UserModel.objects.all()


class BoardList_1(generics.ListCreateAPIView, generics.UpdateAPIView):
    serializer_class = serializers.BoardSerializer_1
    queryset = models.UserModel.objects.all()


class BoardList_2(generics.ListCreateAPIView, generics.UpdateAPIView):
    serializer_class = serializers.BoardSerializer_2
    queryset = models.UserModel.objects.all()


class BoardList_3(generics.ListCreateAPIView, generics.UpdateAPIView):
    serializer_class = serializers.BoardSerializer_3
    queryset = models.UserModel.objects.all()
