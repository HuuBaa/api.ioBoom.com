# _*_ coding: utf-8 _*_
__author__ = 'Huu'
__date__ = '2018/7/16 16:35'

from django.urls import path, include
from rest_framework import routers

from test_api.views import TestApiViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register('test_apis', TestApiViewSet)

urlpatterns = [
    path('', include(router.urls))
]
