from pxl_master.pxl import models
from pxl_master.pxl import serializers
from rest_framework import generics


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
