from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin,RetrieveModelMixin
from .models import Tag,Comment,Article,Subcomment
from .serializers.serializer_v1 import TagListSerializer,TagDetailSerializer,ArticleListSerializer,ArticleDetailSerializer,CommentListSerializer,SubCommentListSerializer

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

class CommentViewSet_v1(GenericViewSet,ListModelMixin,RetrieveModelMixin):
    queryset = Comment.objects.order_by('post_time').all()
    serializer_class = CommentListSerializer


class SubCommentViewSet_v1(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = Subcomment.objects.order_by('post_time').all()
    serializer_class = SubCommentListSerializer