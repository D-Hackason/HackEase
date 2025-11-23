from django.shortcuts import render,get_object_or_404,redirect
from django.views import View
from django.contrib import messages
import re
from requirements.models import Requirements,Articles
from accounts.models import Users
from .models import Base_skills,Base_skills_Requirements

#ユーザーの要件定義一覧表示
class PortralListView(View):
    def get(self,request):
        requirments=Requirements.objects.prefetch_related(
                                        'articles_set',
                                        'requirements_tech_stacks_set__tech_stack_id').all()
        return render(request,"requirements/index.html",{'requirements':requirments})
    
#ユーザーの要件定義詳細表示と応募フォーム
class PortralListDetail(View):
    def get(self,request,id):
        req_detail=Requirements.objects.prefetch_related('articles_set',
                                                        'requirements_tech_stacks_set__tech_stack_id').get(id=id)
        #req_detail=get_object_or_404(Requirements,id=id)これは、image_urlなしの場合
        return render(request,"requirements/detail.html",{'req_detail':req_detail}) #テックスタックも追加する
    
    def post(self,request,id):
        #データベースからの取得（requirementはurlのidから取得可能)
        user_id=request.session.get('id')
        user=Users.objects.get(id=user_id)
        requirement = get_object_or_404(Requirements, id=id)
        #htmlからの取得
        position=request.POST.get("position")
        step=request.POST.get("step")
        commit_time=request.POST.get("commit_time")
        work_time=request.POST.get("work_time")
        git_skill=request.POST.get("git_skill")
        development_experimence=request.POST.get("development_experience")

        base_skill=Base_skills.objects.create(
            user_id=user,
            position=position,
            step=step,
            commit_time=commit_time,
            work_time=work_time,
            git_skill=git_skill,
            development_experimence=development_experimence,
        )
        Base_skills_Requirements.objects.create(
            base_skill_id=base_skill,
            requirement_id=requirement
        )
        return redirect('portral:list')


list=PortralListView.as_view()
list_detail=PortralListDetail.as_view()         