# _*_ coding: utf-8 _*_
__author__ = 'Huu'
__date__ = '2018/8/6 7:51'


from rest_framework import  serializers

from ..models import UserProfile



class UserProfileSerializer_v2(serializers.HyperlinkedModelSerializer):
    articles=serializers.HyperlinkedRelatedField(view_name="articles_v2-detail",read_only=True,many=True)
    sub_comments = serializers.HyperlinkedIdentityField(view_name="subcomments_v2-detail", read_only=True, many=True)
    comments = serializers.HyperlinkedRelatedField(view_name="comments_v2-detail", read_only=True, many=True)
    avatar_url=serializers.SerializerMethodField()
    class Meta:
        model=UserProfile
        fields=('id','username','email','avatar','age','birthday','website','hometown','introduction','avatar_url','articles','sub_comments','comments')

    def get_avatar_url(self,user):
        if user.socialaccount_set.count():
            return user.socialaccount_set.all()[0].get_avatar_url()
        return ""








