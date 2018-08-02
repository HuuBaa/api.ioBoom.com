# _*_ coding: utf-8 _*_
__author__ = 'Huu'
__date__ = '2018/8/2 19:44'

from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth import get_user_model
User=get_user_model()

@receiver(post_save,sender=User)
def create_user(sender,instance=None,created=False,**kwargs):
    if created:
        instance.set_password(instance.password)
        instance.save()