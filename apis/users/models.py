from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class UserProfile(AbstractUser):
    """
    用户
    """
    email = models.EmailField(blank=True, null=True,verbose_name="电子邮箱",help_text="电子邮箱")
    avatar = models.ImageField(blank=True, null=True,upload_to="avatar/",verbose_name="头像",help_text="头像")
    age = models.IntegerField(blank=True, null=True,verbose_name="年龄",help_text="年龄")
    birthday = models.DateField(blank=True, null=True,verbose_name="生日",help_text="生日")
    website = models.URLField(blank=True, null=True,verbose_name="个人网站",help_text="个人网站")
    hometown = models.CharField(max_length=64, blank=True, null=True,verbose_name="家乡",help_text="家乡")
    introduction = models.CharField(max_length=128, blank=True, null=True,verbose_name="个人简介",help_text="个人简介")

    class Meta:
        verbose_name="用户"
        verbose_name_plural="用户"