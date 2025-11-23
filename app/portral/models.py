from django.db import models
from pathlib import Path
from accounts.models import Users
from requirements.models import Requirements

class Base_skills(models.Model):
    user_id=models.ForeignKey(Users,
                            on_delete=models.CASCADE,
                            db_column='user_id',
                            to_field='id',verbose_name='ユーザーID')
    step=models.CharField(max_length=10,null=False,verbose_name='ステップ数')
    work_time=models.TextField(null=False,verbose_name='稼働想定日数')
    commit_time_choices=[
        ('10h','10h'),
        ('15h','15h'),
        ('20h','20h'),
        ('20h~','20h~'),
    ]        
    commit_time=models.CharField(max_length=10,choices=commit_time_choices,null=False,verbose_name="週のコミット時間")
    git_skill_choices=[
        (1,'Git及びGitHubがわからない'),
        (2,'Git及びGitHubは使ったことはあるが、言語化は厳しい'),
        (3,'Git及びGitHubはだいたいわかっていて、人にも説明できる。'),
    ]
    git_skill=models.IntegerField(null=False,choices=git_skill_choices,verbose_name='Git、GitHubについて')
    position_choices=[
        ('frontend','フロント'),
        ('backend','バック'),
        ('infra','インフラ'),
    ]
    position=models.CharField(max_length=255,choices=position_choices,verbose_name='希望ポジション')
    development_experimece_choices=[
        (1,'開発経験なし'),
        (2,'開発経験あり（ハッカソン入門コースのみ・実務未経験）'),
        (3,'実務経験1年未満'),
        (4,'実務経験1年以上'),
    ]
    development_experimence=models.IntegerField(choices=development_experimece_choices,null=False,verbose_name='開発経験について')
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="作成日時")
    updated_at=models.DateTimeField(auto_now=True,verbose_name="更新日時")    

class Base_skills_Requirements(models.Model):
    base_skill_id=models.ForeignKey(Base_skills,
                            on_delete=models.CASCADE,
                            db_column='base_skill_id',
                            to_field='id',verbose_name='応募フォームID')
    requirement_id=models.ForeignKey(Requirements,
                                on_delete=models.CASCADE,
                                db_column='requirement_id',
                                to_field='id',verbose_name='要件定義ID')
    created_at=models.DateTimeField(auto_now_add=True,verbose_name="作成日時")
    updated_at=models.DateTimeField(auto_now=True,verbose_name="更新日時")    
