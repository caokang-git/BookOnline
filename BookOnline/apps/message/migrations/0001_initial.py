# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-09 17:03
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='用户名')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('address', models.CharField(max_length=100, verbose_name='地址')),
                ('message', DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='留言内容')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '用户留言',
                'verbose_name_plural': '用户留言',
                'db_table': 'user_message',
                'ordering': ['-create_time'],
            },
        ),
    ]
