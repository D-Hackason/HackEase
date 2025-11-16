from django.shortcuts import render,redirect
from django.views import View
from django.contrib import messages
import re
import uuid
import hashlib
from .models import Users

EMAIL_PATTERN=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"


class SignupView(View):
    def get(self,request):
        return render(request,"accounts/signup.html")
    
    def post(self,request):
        name=request.POST.get("name")
        e_mail=request.POST.get("email")
        password=request.POST.get("password")
        password_confirmation=request.POST.get("password-confirmation")
        
        if name=="" or e_mail=="" or password=="" or password_confirmation=="":
            messages.error(request,"空のフォームがあります。")
        elif password!=password_confirmation:
            messages.error(request, "2つのパスワードが間違っています。")
        elif not re.match(EMAIL_PATTERN,e_mail):
            messages.error(request,"メールアドレスの形式が正しくありません")
        else:
            id=uuid.uuid4()
            password=hashlib.sha256(password.encode('utf-8')).hexdigest()
            registered_user=Users.objects.filter(e_mail=e_mail).exists()
            if registered_user :
                messages.error(request,"このメールアドレスは存在しています。")
            else:
                UserId=str(id)
                request.session['id']=UserId
                Users.objects.create(
                    id=id,
                    name=name,
                    e_mail=e_mail,
                    password=password
                )
                return render(request,"accounts/success.html")
            return render(request,"accounts/signup.html")   
        return render(request,"accounts/signup.html")   
       

class LoginView(View): 
    def get(self,request):
        return render(request,"accounts/login.html")
    
    def post(self,request):
        e_mail=request.POST.get("email")
        password=request.POST.get("password")

        if e_mail=="" or password=="":
            messages.error(request,"空のフォームがあります")
        else:
            user=Users.objects.filter(e_mail=e_mail).first()
            if user is None:
                messages.error(request,"このユーザーは存在しません")
            else:
                hashpassword=hashlib.sha256(password.encode('utf-8')).hexdigest()
                if hashpassword!=user.password:
                    messages.error(request,"パスワードが間違っています")
                else:
                    request.session['id']=str(user.id)
                    if user.is_admin:
                        return redirect('/requirements/form/')
                    else:
                        return render(request,"accounts/success.html")
        return render(request,"accounts/login.html")
    
class LogoutView(View):
    def get(self,request):
        request.session.flush()
        return redirect("login")
    
login=LoginView.as_view()
signup=SignupView.as_view()
logout=LogoutView.as_view()