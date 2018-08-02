from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,CreateModelMixin

from .models import UserProfile
from .serializers.serializer_v1 import UserProfileSerializer,UserRegisterSerializer
# Create your views here.

class UserProfileViewSet_v1(GenericViewSet,ListModelMixin,RetrieveModelMixin,CreateModelMixin):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    def get_serializer_class(self):
        if self.action=='create':
            return UserRegisterSerializer
        return UserProfileSerializer
