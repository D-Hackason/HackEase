from django.shortcuts import render, redirect
from .forms import QuestionForm

from django.http import HttpResponse

def question_form(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            q = form.save(commit=False)

            # ログインユーザーだけ user を設定する
            if request.user.is_authenticated:
                q.user = request.user
            
            q.save()
            return redirect('inquiry:success')
    else:
        form = QuestionForm()
    
    return render(request, 'inquiry/question_form.html', {'form': form})


def success(request):
    return render(request, 'inquiry/success.html')