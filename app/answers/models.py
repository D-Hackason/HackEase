from django.db import models
from accounts.models import Users

# 回答フォーム

class Answers(models.Model):
    
    user = models.ForeignKey(
    Users,
    on_delete=models.CASCADE,
    related_name='answer_users',
    null=True,
    blank=True
    )
    question = models.ForeignKey(
    'inquiry.Question',
    on_delete=models.CASCADE,
    related_name='answers'
    )

    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)    # 自動で現在時刻セット
    updated_at = models.DateTimeField(auto_now=True)     # 自動で更新時刻セット


    def __str__(self):
        return self.name