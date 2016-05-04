from pxl import models
from pxl import serializers
from rest_framework import generics
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import AllowAny
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
        user = User.objects.get(username=request.data['username'])
        if user.password == request.data['password']:
            tok = Token.objects.get(user=user)
            content = {
                'token': str(tok)
            }
        else:
            return HttpResponse('Unauthorized', status=401)
        return Response(content)


class BoardList(generics.ListCreateAPIView, generics.UpdateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = serializers.BoardSerializer
    # queryset = models.PXLBoardModel.objects.all()

    def get_queryset(self):
        import pdb; pdb.set_trace()
        token = Token.objects.get(key=self.request.data['token'])
        user = User.objects.get(username=token.user.username)
        return models.PXLBoardModel.objects.get(owner=user)

    def perform_create(self, serializer):
        import pdb; pdb.set_trace()
        token = Token.objects.get(key=self.request.data['token'])
        user = User.objects.get(username=token.user.username)
        serializer.save(owner=user)

    def perform_update(self, serializer):
        import pdb; pdb.set_trace()
        token = Token.objects.get(key=self.request.data['token'])
        user = User.objects.get(username=token.user.username)
        serializer.save(owner=user)
