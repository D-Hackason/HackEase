from django.shortcuts import render, redirect
from .forms import QuestionForm

from django.http import JsonResponse
from .models import Question

# 質問一覧 GET
def question_list(request):
    questions = Question.objects.all().order_by('-created_at')
    
    data = [{
        "id": q.id,
        "title": q.title,
        "team_name": q.team_name,
        "category": q.category,
        "content": q.content,
        "is_answer": q.is_answer,
        "created_at": q.created_at,
        "updated_at": q.updated_at,
    } for q in questions]

    return JsonResponse({"questions": data}, json_dumps_params={'ensure_ascii': False})

# 質問詳細 GET（回答も含める）
def question_detail(request, question_id):
    try:
        q = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        return JsonResponse({"error": "Question not found"}, status=404)

    # 回答一覧
    answer_list = [{
        "id": a.id,
        "user": str(a.user),
        "content": a.content,
        "created_at": a.created_at,
    } for a in q.answers.all()]

    data = {
        "id": q.id,
        "title": q.title,
        "team_name": q.team_name,
        "category": q.category,
        "content": q.content,
        "is_answer": q.is_answer,
        "created_at": q.created_at,
        "updated_at": q.updated_at,
        "answers": answer_list,
    }

    return JsonResponse(data, json_dumps_params={'ensure_ascii': False})


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

    return render(request, 'FAQ/index.html', {'form': form})


def success(request):
    return render(request, 'inquiry/success.html')