from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
import re
from .models import Requirements,Articles
from accounts.models import Users
from django.contrib.auth.decorators import login_required

class RequirementFormView(View):
    def get(self,request):
        return render(request,"requirements/form.html")

    def post(self,request):
        user_id=request.session.get('id')
        user=Users.objects.get(id=user_id)

        title=request.POST.get("title")
        content=request.POST.get("content")
        participants=request.POST.get("participants")
        tech=request.POST.get("tech")
        team=request.POST.get("team")
        save_type=request.POST.get("save_type")
        if save_type=="private":
            is_public=True
        else:
            is_public=False
        
        requirement=Requirements.objects.create(
            user_id=user,
            title=title,
            content=content,
            team=team,
            participants=participants,
            tech=tech,
            is_public=is_public
        )

        categories={
            'frontend':('frontend-title','frontend-url'),
            'backend':('backend-title','backend-url'),  
            'infra':('infra-title','infra-url')}
        for category,(title_list,url_list) in categories.items():
            titles=request.POST.getlist(title_list)
            urls=request.POST.getlist(url_list)
            for title,url in zip(titles,urls):
                if title and url:
                    Articles.objects.create(
                        requirement_id=requirement,
                        categories=category,
                        title=title,
                        url=url,
                    )
        return render(request,'requirements/success.html')

  
        

form=RequirementFormView.as_view()
        
        




        







