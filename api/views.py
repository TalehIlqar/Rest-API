from django.shortcuts import render

from django.contrib.auth import get_user_model
from rest_framework.response import Response

from rest_framework import viewsets, permissions
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from api.serializers import UserSerializer, UserListSerializer

from user.models import User


User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    queryset = User.objects.all()


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ListUserAPIView(ListAPIView):
    serializer_class = UserListSerializer
    permission_classes = (IsAuthenticated,)


    def get(self, request, pk=None):
        return Response(UserListSerializer(request.user).data)