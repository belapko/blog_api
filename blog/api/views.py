from rest_framework import generics
from . import serializers
from django.contrib.auth.models import User


class UserList(generics.ListAPIView):  # get collection
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):  # get single model
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
