from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,CreateModelMixin,UpdateModelMixin
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail

import random
from .models import UserProfile,VerifyCode
from .serializers.serializer_v1 import UserUpdateSerializer,UserProfileSerializer,UserRegisterSerializer,VerifyCodeSerializer
from .permissions import IsOwnerOrReadOnly
# Create your views here.

class UserProfileViewSet_v1(GenericViewSet,ListModelMixin,RetrieveModelMixin,CreateModelMixin,UpdateModelMixin):
    """
    list:
        全部用户列表
    retrieve:
        单个用户信息
    create:
        注册用户
    partial_update:
        更新用户资料
    update:
        更新用户资料
    """
    queryset = UserProfile.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)
    def get_serializer_class(self):
        if self.action=='create':
            return UserRegisterSerializer
        if self.action in ['update','partial_update']:
            return UserUpdateSerializer
        return UserProfileSerializer

class VerifyCodeViewSet_v1(GenericViewSet,CreateModelMixin):
    serializer_class = VerifyCodeSerializer

    def gen_code(self):
        seed="0123456789abcdefghxyz"
        code=[]
        for i in range(6):
            code.append(random.choice(seed))
        return "".join(code)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = self.gen_code()

        mail_body = "欢迎您在ioboom.com注册！<br>您的验证码是:{0}".format(code)
        try:
            send_mail("注册验证码", mail_body, "ioboom管理员<ioboom@ioboom.com>", [serializer.validated_data["email"]])
        except Exception as e:
            return Response({
                "email": "邮件发送出错，请重试"
            }, status=status.HTTP_400_BAD_REQUEST)

        code_record = VerifyCode(code=code, email=serializer.validated_data["email"])
        code_record.save()
        return Response({
            "email": code_record.email
        }, status=status.HTTP_201_CREATED)




