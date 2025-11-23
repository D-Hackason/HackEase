from django.db import models
from accounts.models import Users

# 問い合わせフォーム

class Question(models.Model):
    
    CATEGORY_CHOICES = [
        ("フロントエンド", "frontend"),
        ("バックエンド", "backend"),
        ("インフラ", "infra"),
    ]
    
    user = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name='questions',
        null=True,
        blank=True
    )
    title = models.CharField(max_length=255, verbose_name="タイトル")
    team_name = models.CharField(max_length=32, verbose_name="チーム名")
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    content = models.TextField()
    is_answer = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)    # 自動で現在時刻セット
    updated_at = models.DateTimeField(auto_now=True)     # 自動で更新時刻セット

    class Meta:
        db_table = "questions"

    def __str__(self):
        return f"{self.name} - {self.subject}"