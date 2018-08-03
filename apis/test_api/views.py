from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework import permissions

from .models import TestApiModel
from .serializers.serializers import TestApiSerializer
from .serializers.serializers_v1 import TestApiSerializer_v1


class TestApiViewSet(ModelViewSet):
    """
    list:
        获取test_api列表
    """
    queryset = TestApiModel.objects.all()
    serializer_class = TestApiSerializer
    filter_backends = (DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter)
    filter_fields=('name',)
    ordering_fields=('numbers','time')
    search_fields=('content','name')
    permission_classes = (permissions.IsAuthenticated,)

class TestApiViewSet_v1(TestApiViewSet):
    serializer_class = TestApiSerializer_v1