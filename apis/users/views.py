from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import os
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,CreateModelMixin,UpdateModelMixin
from rest_framework.response import Response
from rest_framework import status,pagination,permissions
from rest_framework_jwt.serializers import jwt_payload_handler,jwt_encode_handler

from django.core.mail import send_mail
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

import random
from .models import UserProfile,VerifyCode
from .serializers.serializer_v1 import UserUpdateSerializer,UserProfileSerializer,UserRegisterSerializer,VerifyCodeSerializer,UserJWTSerializer
from .serializers.serializer_v2 import UserProfileSerializer_v2
from .permissions import IsOwnerOrReadOnly
# Create your views here.

class CustomBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user=UserProfile.objects.get(Q(username=username)|Q(email=username))
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
        except Exception as e:
            return None

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
    queryset = UserProfile.objects.order_by("-id").all()
    permission_classes = (IsOwnerOrReadOnly,)
    #pagination_class = pagination.LimitOffsetPagination
    def get_serializer_class(self):
        if self.action=='create':
            return UserRegisterSerializer
        if self.action in ['update','partial_update']:
            return UserUpdateSerializer
        return UserProfileSerializer

    def perform_create(self, serializer):
        return serializer.save()
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        #注册成功后返回token和user信息
        user=self.perform_create(serializer)
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        res_dict=serializer.data
        res_dict["user"]=UserJWTSerializer(user, context={'request': request}).data
        res_dict["token"]=token

        headers = self.get_success_headers(serializer.data)
        return Response(res_dict, status=status.HTTP_201_CREATED, headers=headers)


class VerifyCodeViewSet_v1(GenericViewSet,CreateModelMixin):
    """
    邮箱验证码
    """
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
            "email": code_record.email,
        }, status=status.HTTP_201_CREATED)



#v2 api
class UserProfileViewSet_v2(GenericViewSet,ListModelMixin,RetrieveModelMixin):
    """
    list:
        全部用户列表
    retrieve:
        单个用户信息
    """
    queryset = UserProfile.objects.order_by("-id").all()
    serializer_class = UserProfileSerializer_v2


class SocialTokenView(APIView):
    """
    第三方登录后，跳转到这个url，可以获取到jwt token
    """
    permission_classes = (permissions.IsAuthenticated,)
    def get(self,request):
        user = request.user
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        res_dict={}
        res_dict["user"] = UserJWTSerializer(user, context={'request': request}).data
        res_dict["token"] = token
        return Response(res_dict, status=status.HTTP_201_CREATED)