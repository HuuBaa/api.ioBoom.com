# _*_ coding: utf-8 _*_
__author__ = 'Huu'
__date__ = '2018/8/2 16:14'

from rest_framework import  serializers
from rest_framework.validators import UniqueValidator
from datetime import datetime,timedelta

from ..models import UserProfile,VerifyCode


class UserProfileSerializer(serializers.ModelSerializer):
    avatar_url=serializers.SerializerMethodField()

    class Meta:
        model=UserProfile
        fields=('id','username','email','avatar','age','birthday','website','hometown','introduction','avatar_url')

    def get_avatar_url(self,user):
        if user.socialaccount_set.count():
            return user.socialaccount_set.all()[0].get_avatar_url()
        return ""


class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserProfile
        fields=('avatar','age','birthday','website','hometown','introduction')


class UserRegisterSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(help_text="请输入格式正确的电子邮箱",label="电子邮箱",
                                 validators=[UniqueValidator(queryset=UserProfile.objects.all(),message="邮箱已经注册")]
                                 )
    password=serializers.CharField(min_length=6,max_length=128,help_text="密码",label="密码",
                                   error_messages={
                                       "min_length":"密码至少要有6个字符"
                                   },write_only=True,style={"input_type":"password"})
    password2=serializers.CharField(min_length=6,max_length=128,help_text="重复密码",label="重复密码",
                                   error_messages={
                                       "min_length":"密码至少要有6个字符",
                                   },write_only=True,style={"input_type":"password"})

    code=serializers.CharField(write_only=True,max_length=6,min_length=6,label="验证码",help_text="验证码",error_messages={
        "required":"请填写验证码",
        "min_length":"验证码格式错误",
        "max_length": "验证码格式错误"
    })

    def validate_code(self,code):
        code_record=VerifyCode.objects.filter(email=self.initial_data["email"]).order_by("-add_time")
        if code_record:
            last_code=code_record[0]
            half_hour_ago=datetime.now()-timedelta(minutes=30)
            if half_hour_ago>last_code.add_time:
                raise serializers.ValidationError("验证码已经过期")
            if last_code.code!=code:
                raise serializers.ValidationError("验证码错误")
        else:
            raise serializers.ValidationError("验证码错误")


    def validate(self,data):
        if data['password']!=data['password2']:
            raise serializers.ValidationError("两次输入密码不一致")
        del data['password2']
        del data['code']
        return data

    class Meta:
        model=UserProfile
        fields=('username','email','password','password2','code')


class VerifyCodeSerializer(serializers.Serializer):
    email = serializers.EmailField(help_text="请输入格式正确的电子邮箱", label="电子邮箱",
                                   validators=[UniqueValidator(queryset=UserProfile.objects.all(), message="邮箱已经注册")]
                                   )
    def validate_email(self,email):
        one_minute_ago = datetime.now() - timedelta(minutes=1)
        if VerifyCode.objects.filter(email=email,add_time__gt=one_minute_ago).count():
            raise serializers.ValidationError("请在一分钟后再次请求验证码")
        return email