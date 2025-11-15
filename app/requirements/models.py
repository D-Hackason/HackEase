from django.db import models
import uuid
from pathlib import Path
from accounts.models import Users

class Requirements(models.Model):
    user_id=models.ForeignKey(Users,
                           on_delete=models.CASCADE,
                           db_column='user_id',
                           to_field='id',verbose_name='ユーザーID')
    title=models.CharField(max_length=255,null=False,verbose_name='タイトル')
    content=models.TextField(null=False,verbose_name='内容')
    participants=models.IntegerField(default=0,verbose_name='参加人数')
    tech=models.TextField(null=False,verbose_name='使用技術')
    team=models.CharField(null=False,max_length=255,verbose_name='チーム名')
    is_public=models.BooleanField(default=False,verbose_name='公表、非公表')
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="作成日時")
    updated_at=models.DateTimeField(auto_now=True,verbose_name="更新日時")
    #teamって入れる？　使用技術はtechで一旦保存#

class Articles(models.Model):
    requirement_id=models.ForeignKey(Requirements,
                                     on_delete=models.CASCADE,
                                     db_column='requirements_id',
                                     to_field='id')
    category_choices=[
        ('frontend','フロントエンド'),
        ('backend','バックエンド'),
        ('infra','インフラ')
    ]
    categories=models.CharField(max_length=20,
                                choices=category_choices,
                                null=False,
                                verbose_name='カテゴリー')
    title=models.CharField(max_length=255,null=False,verbose_name='タイトル')
    url=models.TextField(null=False,verbose_name='url')
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="作成日時")
    updated_at=models.DateTimeField(auto_now=True,verbose_name="更新日時")

