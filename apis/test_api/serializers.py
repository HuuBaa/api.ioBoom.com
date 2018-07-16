# _*_ coding: utf-8 _*_
__author__ = 'Huu'
__date__ = '2018/7/16 16:24'

from rest_framework import serializers

from .models import TestApiModel

class TestApiSerializer(serializers.ModelSerializer):

    class Meta:
        model=TestApiModel
        fields="__all__"