from pxl import models
from pxl import serializers
from rest_framework import generics
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from django.http import HttpResponse


class RegisterView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.UserSerializer1


class LoginView(APIView):
    """Registration and login view."""
    permission_classes = (AllowAny,)
    serializer_class = serializers.UserLoginSerializer

    def post(self, request, format=None):
        """Return user and authorization to front end."""
        import pdb; pdb.set_trace()
        user = User.objects.get(username=request.data['username'])
        if user.password == request.data['password']:
            tok = Token.objects.get(user=user)
            content = {
                'token': str(tok)
            }
        else:
            return HttpResponse('Unauthorized', status=401)
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
