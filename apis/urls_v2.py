# _*_ coding: utf-8 _*_
__author__ = 'Huu'
__date__ = '2018/8/6 6:54'

from django.urls import path, include
from rest_framework import routers

from articles.views import TagViewSet_v2,ArticleViewSet_v2,CommentViewSet_v2,SubCommentViewSet_v2
from users.views import UserProfileViewSet_v2

router = routers.DefaultRouter(trailing_slash=False)
router.register('users', UserProfileViewSet_v2,base_name="users_v2")
router.register('tags', TagViewSet_v2,base_name="tags_v2")
router.register('articles', ArticleViewSet_v2,base_name="articles_v2")
router.register('comments', CommentViewSet_v2,base_name="comments_v2")
router.register('subcomments', SubCommentViewSet_v2,base_name="subcomments_v2")

urlpatterns = [
    path('v2/', include(router.urls))
]
