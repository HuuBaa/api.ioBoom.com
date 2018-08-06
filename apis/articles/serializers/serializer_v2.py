# _*_ coding: utf-8 _*_
__author__ = 'Huu'
__date__ = '2018/8/6 6:52'

from rest_framework import serializers
from ..models import Tag,Subcomment,Comment,Article

class TagListSerializer_v2(serializers.HyperlinkedModelSerializer):
    """
    标签list
    """
    url=serializers.HyperlinkedIdentityField(view_name="tags_v2-detail")
    class Meta:
        model=Tag
        fields="__all__"


class ArticleListSerializer_v2(serializers.HyperlinkedModelSerializer):
    """
    文章list
    """
    url=serializers.HyperlinkedIdentityField(view_name="articles_v2-detail")
    author=serializers.HyperlinkedRelatedField(view_name="users_v2-detail",read_only=True)
    tags=serializers.HyperlinkedRelatedField(view_name="tags_v2-detail",read_only=True,many=True)
    comment_count=serializers.SerializerMethodField()
    class Meta:
        model = Article
        exclude = ("content",)
    #获取评论总数
    def get_comment_count(self,article):
        sub_count=0
        for comment in article.comments.all():
            sub_count+=comment.sub_comments.count()
        return article.comments.count()+sub_count

class SubCommentListSerializer_v2(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="subcomments_v2-detail")
    author = serializers.HyperlinkedRelatedField(view_name="users_v2-detail",read_only=True)
    reply_to=serializers.HyperlinkedRelatedField(view_name="users_v2-detail",read_only=True)
    article = serializers.HyperlinkedRelatedField(view_name="articles_v2-detail", read_only=True)
    parent_comment = serializers.HyperlinkedRelatedField(view_name="comments_v2-detail", read_only=True)
    class Meta:
        model=Subcomment
        fields="__all__"

class CommentListSerializer_v2(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="comments_v2-detail")
    author = serializers.HyperlinkedRelatedField(view_name="users_v2-detail",read_only=True)
    sub_comments=serializers.HyperlinkedIdentityField(view_name="subcomments_v2-detail",read_only=True,many=True)
    article=serializers.HyperlinkedRelatedField(view_name="articles_v2-detail",read_only=True)
    class Meta:
        model=Comment
        fields="__all__"


class TagDetailSerializer_v2(serializers.HyperlinkedModelSerializer):
    """
    文章retrieve
    """
    url = serializers.HyperlinkedIdentityField(view_name="tags_v2-detail")
    articles=serializers.HyperlinkedRelatedField(view_name="articles_v2-detail",read_only=True,many=True)
    class Meta:
        model=Tag
        fields="__all__"


class ArticleDetailSerializer_v2(serializers.HyperlinkedModelSerializer):
    """
    文章retrieve
    """
    url=serializers.HyperlinkedIdentityField(view_name="articles_v2-detail")
    author=serializers.HyperlinkedRelatedField(view_name="users_v2-detail",read_only=True)
    tags=serializers.HyperlinkedRelatedField(view_name="tags_v2-detail",read_only=True,many=True)
    comments=serializers.HyperlinkedRelatedField(view_name="comments_v2-detail",read_only=True,many=True)
    class Meta:
        model = Article
        fields = "__all__"


