from django.db import models
from datetime import datetime
# Create your models here.
class TestApiModel(models.Model):
    id=models.IntegerField(verbose_name="id",help_text="id",primary_key=True)
    name=models.CharField(max_length=100,verbose_name="名字",help_text="名字")
    numbers=models.BigIntegerField(verbose_name="数量",help_text="数量")
    time=models.DateTimeField(verbose_name="时间",help_text="时间",default=datetime.now)
    content=models.TextField(verbose_name="内容啊",help_text="内容啊")

    def __str__(self):
        return "测试api(id:{0})".format(self.id)

    class Meta:
        verbose_name="测试apiModel"
        verbose_name_plural=verbose_name