from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from django_filters.rest_framework.backends import DjangoFilterBackend
from .models import TestApiModel
from .serializers import TestApiSerializer

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

