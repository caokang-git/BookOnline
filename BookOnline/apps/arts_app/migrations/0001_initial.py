# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-09 17:03
from __future__ import unicode_literals

import DjangoUeditor.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Art',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_title', models.CharField(max_length=100, verbose_name='文章标题')),
                ('a_info', models.CharField(max_length=200, verbose_name='文章描述')),
                ('a_content', DjangoUeditor.models.UEditorField(blank=True, default='', verbose_name='文章内容')),
                ('a_img', models.ImageField(blank=True, max_length=150, null=True, upload_to='arts_ups/%Y/%m', verbose_name='封面')),
                ('a_createtime', models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='添加时间')),
                ('a_price', models.IntegerField(default=0, verbose_name='单价')),
                ('a_flag', models.IntegerField(choices=[(0, '默认'), (1, '待删除'), (2, '已删除')], default=0, verbose_name='控制字段')),
            ],
            options={
                'verbose_name': '小说',
                'verbose_name_plural': '小说',
                'db_table': 'art',
                'ordering': ['-a_createtime'],
            },
        ),
        migrations.CreateModel(
            name='ArtsUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, verbose_name='用户名')),
                ('password', models.CharField(max_length=80, verbose_name='密码')),
                ('email', models.EmailField(max_length=254, verbose_name='邮箱')),
                ('createtime', models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='添加时间')),
                ('flag', models.IntegerField(choices=[(0, '默认'), (1, '待删除'), (2, '已删除')], default=0, verbose_name='控制字段')),
            ],
            options={
                'verbose_name': '会员信息',
                'verbose_name_plural': '会员信息',
                'db_table': 'arts_user',
                'ordering': ['-createtime'],
            },
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='章节标题')),
                ('content', models.TextField(verbose_name='小说章节内容')),
                ('create_time', models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='添加时间')),
                ('art', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arts_app.Art', verbose_name='小说')),
            ],
            options={
                'verbose_name': '小说章节',
                'verbose_name_plural': '小说章节',
                'db_table': 'art_chapter',
            },
        ),
        migrations.CreateModel(
            name='LineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='单价')),
                ('quantity', models.IntegerField(verbose_name='数量')),
                ('createtime', models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='添加购物车时间')),
                ('flag', models.IntegerField(choices=[(0, '待下单'), (1, '已下单')], default=0, verbose_name='控制字段')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arts_app.Art', verbose_name='文章商品')),
            ],
            options={
                'verbose_name': '商品条目',
                'verbose_name_plural': '商品条目',
                'db_table': 'line_item',
            },
        ),
        migrations.CreateModel(
            name='ProductOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(unique=True, verbose_name='订单号')),
                ('pay_type', models.IntegerField(choices=[(0, '货到付款'), (1, '微信支付'), (2, '支付宝支付')], default=0, verbose_name='控制字段')),
                ('address', models.CharField(default='', max_length=100, verbose_name='订单配送地址')),
                ('phone', models.IntegerField(default=0, verbose_name='订单配送电话')),
                ('order_time', models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='下单时间')),
            ],
            options={
                'verbose_name': '用户订单',
                'verbose_name_plural': '用户订单',
                'db_table': 'product_order',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='学生姓名')),
                ('sex', models.CharField(choices=[('M', '男人'), ('F', '女人')], default='female', max_length=10, verbose_name='性别')),
                ('address', models.CharField(max_length=10, verbose_name='地址')),
                ('addtime', models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='添加时间')),
                ('flag', models.IntegerField(choices=[(0, '默认'), (1, '待删除'), (2, '已删除')], default=0, verbose_name='控制字段')),
            ],
            options={
                'verbose_name': '学生信息',
                'verbose_name_plural': '学生信息',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('t_name', models.CharField(max_length=20, verbose_name='文章标签')),
                ('t_info', models.CharField(max_length=50, verbose_name='标签描述')),
                ('t_createtime', models.DateTimeField(db_index=True, default=django.utils.timezone.now, verbose_name='创建时间')),
                ('t_flag', models.IntegerField(choices=[(0, '默认'), (1, '待删除'), (2, '已删除')], default=0, verbose_name='控制字段')),
            ],
            options={
                'verbose_name': '标签',
                'verbose_name_plural': '标签',
                'db_table': 'tag',
                'ordering': ['-t_createtime'],
            },
        ),
        migrations.AddField(
            model_name='lineitem',
            name='product_order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='arts_app.ProductOrder', to_field='order_id', verbose_name='订单'),
        ),
        migrations.AddField(
            model_name='lineitem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arts_app.ArtsUser', verbose_name='购买者'),
        ),
        migrations.AddField(
            model_name='art',
            name='a_tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arts_app.Tag', verbose_name='关联文章标签'),
        ),
        migrations.AddField(
            model_name='art',
            name='operator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
