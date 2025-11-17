from django.db import models
import uuid
from pathlib import Path

class Users(models.Model):
    id=models.UUIDField(primary_key=True,default=False,editable=False,verbose_name="ID")
    name=models.CharField(max_length=100,null=False,verbose_name="名前")
    e_mail=models.CharField(max_length=255,null=False,verbose_name="メールアドレス")
    password=models.CharField(max_length=255,null=False,verbose_name="パスワード")
    is_admin=models.BooleanField(default=False,verbose_name="管理者")
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="作成日時")
    updated_at=models.DateTimeField(auto_now=True,verbose_name="更新日時")    