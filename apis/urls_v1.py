# _*_ coding: utf-8 _*_
__author__ = 'Huu'
__date__ = '2018/7/16 16:35'

from django.urls import path, include
from rest_framework import routers

from test_api.views import TestApiViewSet_v1
from users.views import UserProfileViewSet_v1,VerifyCodeViewSet_v1
from articles.views import TagViewSet_v1,ArticleViewSet_v1,CommentViewSet_v1,SubCommentViewSet_v1

router = routers.DefaultRouter(trailing_slash=False)
#router.register('test_apis', TestApiViewSet_v1,base_name="test_api_v1")
router.register('users', UserProfileViewSet_v1,base_name="users_v1")
router.register('code', VerifyCodeViewSet_v1,base_name="code_v1")
router.register('tags', TagViewSet_v1,base_name="tags_v1")
router.register('articles', ArticleViewSet_v1,base_name="articles_v1")
router.register('comments', CommentViewSet_v1,base_name="comments_v1")
router.register('subcomments', SubCommentViewSet_v1,base_name="subcomments_v1")

urlpatterns = [
    path('v1/', include(router.urls))
]
