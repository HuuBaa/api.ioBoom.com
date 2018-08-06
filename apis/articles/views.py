from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin,CreateModelMixin
from .models import Tag,Comment,Article,Subcomment
from .serializers.serializer_v1 import TagListSerializer,TagDetailSerializer,ArticleListSerializer,ArticleDetailSerializer,CommentListSerializer,SubCommentListSerializer,CommentCreateSerializer,SubCommentCreateSerializer
from .serializers.serializer_v2 import  TagListSerializer_v2,TagDetailSerializer_v2,ArticleListSerializer_v2,ArticleDetailSerializer_v2,CommentListSerializer_v2,SubCommentListSerializer_v2
from rest_framework import permissions

class TagViewSet_v1(GenericViewSet,ListModelMixin,RetrieveModelMixin):
    queryset = Tag.objects.all()
    def get_serializer_class(self):
        if self.action=="list":
            return TagListSerializer
        return TagDetailSerializer

class ArticleViewSet_v1(GenericViewSet,ListModelMixin,RetrieveModelMixin):
    queryset = Article.objects.order_by('-post_time').all()
    def get_serializer_class(self):
        if self.action=="list":
            return ArticleListSerializer
        return ArticleDetailSerializer

class CommentViewSet_v1(GenericViewSet,ListModelMixin,RetrieveModelMixin,CreateModelMixin):
    queryset = Comment.objects.order_by('post_time').all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def get_serializer_class(self):
        if self.action=='create':
            return CommentCreateSerializer
        return CommentListSerializer


class SubCommentViewSet_v1(GenericViewSet, ListModelMixin, RetrieveModelMixin,CreateModelMixin):
    queryset = Subcomment.objects.order_by('post_time').all()
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    def get_serializer_class(self):
        if self.action=='create':
            return SubCommentCreateSerializer
        return SubCommentListSerializer


#v2 api start

class TagViewSet_v2(GenericViewSet,ListModelMixin,RetrieveModelMixin):
    queryset = Tag.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return TagListSerializer_v2
        return TagDetailSerializer_v2

class ArticleViewSet_v2(GenericViewSet,ListModelMixin,RetrieveModelMixin):
    queryset = Article.objects.order_by('-post_time').all()
    def get_serializer_class(self):
        if self.action=="list":
            return ArticleListSerializer_v2
        return ArticleDetailSerializer_v2

class CommentViewSet_v2(GenericViewSet,ListModelMixin,RetrieveModelMixin):
    queryset = Comment.objects.order_by('post_time').all()
    serializer_class = CommentListSerializer_v2


class SubCommentViewSet_v2(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Subcomment.objects.order_by('post_time').all()
    serializer_class = SubCommentListSerializer_v2
