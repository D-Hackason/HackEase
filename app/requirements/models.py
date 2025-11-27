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
    difficulty = models.CharField(max_length=10, choices=[
    ('low', '初級'),
    ('mid', '中級'),
    ('high', '上級'),
    ], default='mid',verbose_name='難易度')
    participants=models.IntegerField(default=0,verbose_name='参加人数')
    #techは削除
    team=models.CharField(null=False,max_length=255,verbose_name='チーム名')
    is_public=models.BooleanField(default=False,verbose_name='公表、非公表')
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="作成日時")
    updated_at=models.DateTimeField(auto_now=True,verbose_name="更新日時")

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

class tech_stacks(models.Model):
    title=models.CharField(max_length=63,null=False,verbose_name='技術名')
    img_url=models.URLField(null=False,verbose_name='画像のurl')
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="作成日時")
    updated_at=models.DateTimeField(auto_now=True,verbose_name="更新日時")

class requirements_tech_stacks(models.Model):
    requirement_id=models.ForeignKey(Requirements,
                                     on_delete=models.CASCADE,
                                     db_column='requirements_id',
                                     to_field='id')
    tech_stack_id=models.ForeignKey(tech_stacks,
                                     on_delete=models.CASCADE,
                                     db_column='tech_stack_id',
                                     to_field='id')
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="作成日時")
    updated_at=models.DateTimeField(auto_now=True,verbose_name="更新日時")