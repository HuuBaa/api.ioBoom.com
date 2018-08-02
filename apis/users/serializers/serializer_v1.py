# _*_ coding: utf-8 _*_
__author__ = 'Huu'
__date__ = '2018/8/2 16:14'

from rest_framework import  serializers
from rest_framework.validators import UniqueValidator
from ..models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields=('id','username','email','avatar','age','birthday','website','hometown','introduction')

class UserRegisterSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(help_text="格式正确的电子邮箱",label="电子邮箱",validators=[UniqueValidator(queryset=UserProfile.objects.all(),message="邮箱已经被注册")])
    password=serializers.CharField(min_length=6,max_length=128,help_text="密码",label="密码",
                                   error_messages={
                                       "min_length":"密码至少要有6个字符"
                                   },write_only=True)
    password2=serializers.CharField(min_length=6,max_length=128,help_text="重复密码",label="重复密码",
                                   error_messages={
                                       "min_length":"密码至少要有6个字符",
                                   },write_only=True)

    def validate(self,data):
        if data['password']!=data['password2']:
            raise serializers.ValidationError("两次输入密码不一致")
        del data['password2']
        return data

    class Meta:
        model=UserProfile
        fields=('username','email','password','password2')