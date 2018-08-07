from django.db import models

# Create your models here.

from django.db import models

from datetime import datetime
from django.template.defaultfilters import slugify
from django.conf import settings
from django.contrib.auth import get_user_model

User=get_user_model()

class Article(models.Model):
    ""
    title=models.CharField(max_length=128,verbose_name="标题",help_text="标题")
    post_time=models.DateTimeField(default=datetime.now,verbose_name="发布时间",help_text="发布时间")
    author=models.ForeignKey(User,related_name='articles',on_delete=models.CASCADE,verbose_name="作者",help_text="作者")
    content=models.TextField(max_length=1024*20,verbose_name="内容",help_text="内容")
    summary=models.TextField(max_length=514,verbose_name="摘要",help_text="摘要")
    picture=models.ImageField(blank=True,null=True,upload_to='article_images',verbose_name="主图",help_text="主图")
    #Tag的实例可以使用t.articles查询相应tag下所有的article
    tags = models.ManyToManyField('Tag',blank=True,related_name='articles',verbose_name="标签",help_text="标签")
    likes=models.IntegerField(default=0,verbose_name="点赞数",help_text="点赞数")
    views=models.IntegerField(default=0,verbose_name="阅读数",help_text="阅读数")

    class Meta:
        verbose_name="文章"
        verbose_name_plural=verbose_name


    def __str__(self):
        return self.title

class Tag(models.Model):
    name=models.CharField(max_length=32,unique=True,verbose_name="标签名",help_text="标签名")
    chinese_name=models.CharField(blank=True,null=True,max_length=32,verbose_name="标签中文名",help_text="标签中文名")
    slug=models.SlugField(blank=True,unique=True,verbose_name="标签slug",help_text="标签slug")
    desc=models.CharField(max_length=128,blank=True,null=True,verbose_name="标签描述",help_text="标签描述")

    def save(self, *args, **kw):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kw)

    class Meta:
        verbose_name="标签"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name

class Comment(models.Model):
    author=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="评论人",help_text="评论人",related_name='comments')
    content=models.TextField(max_length=256,verbose_name="评论内容",help_text="评论内容")
    post_time=models.DateTimeField(default=datetime.now,verbose_name="评论时间",help_text="评论时间")
    article=models.ForeignKey('Article',related_name='comments',on_delete=models.CASCADE,verbose_name="从属文章",help_text="从属文章")

    class Meta:
        verbose_name="一级评论"
        verbose_name_plural=verbose_name

    def __str__(self):
        return '一级评论<id:%s> 评论人:%s 文章:%s '%(self.id,self.author,self.article)

class Subcomment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="评论人",help_text="评论人",related_name='sub_comments')
    content = models.TextField(max_length=256,verbose_name="评论内容",help_text="评论内容")
    post_time = models.DateTimeField(default=datetime.now,verbose_name="评论时间",help_text="评论时间")
    article = models.ForeignKey('Article',on_delete=models.CASCADE,verbose_name="从属文章",help_text="从属文章")
    parent_comment=models.ForeignKey(Comment,related_name='sub_comments',on_delete=models.CASCADE,verbose_name="父评论",help_text="父评论")
    reply_to=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="回复给",help_text="回复给")

    class Meta:
        verbose_name="二级评论"
        verbose_name_plural=verbose_name

    def __str__(self):
        return '二级评论<id:%s>  回复给:%s 文章:%s'%(self.id,self.reply_to,self.article)

