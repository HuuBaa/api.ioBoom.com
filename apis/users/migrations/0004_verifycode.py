# Generated by Django 2.0.7 on 2018-08-03 09:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20180803_0816'),
    ]

    operations = [
        migrations.CreateModel(
            name='VerifyCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(help_text='电子邮箱', max_length=254, verbose_name='电子邮箱')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, help_text='添加时间', verbose_name='添加时间')),
                ('code', models.CharField(max_length=6, verbose_name='验证码')),
            ],
            options={
                'verbose_name': '邮箱验证码',
                'verbose_name_plural': '邮箱验证码',
            },
        ),
    ]
