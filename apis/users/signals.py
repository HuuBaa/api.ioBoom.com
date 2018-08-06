# _*_ coding: utf-8 _*_
__author__ = 'Huu'
__date__ = '2018/8/2 19:44'

from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.socialaccount.signals import pre_social_login
from allauth.socialaccount.models import SocialAccount,SocialLogin

from django.contrib.auth import get_user_model
User=get_user_model()

@receiver(post_save,sender=User)
def create_user(sender,instance=None,created=False,**kwargs):
    if created:
        print(instance.password)
        instance.set_password(instance.password)
        instance.save()

#使用allauth的信号量
# @receiver(pre_social_login,sender=SocialLogin)
# def pre_login(sender,sociallogin=None,**kwargs):
#     sociallogin.user.avatar_url=sociallogin.account.extra_data["avatar_url"]
#     sociallogin.user.save()

