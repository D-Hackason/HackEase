from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Answers
from inquiry.models import Question
from accounts.models import Users
from django.shortcuts import render, redirect

import json

@csrf_exempt
def create_answer(request, question_id):
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=400)

    content = request.POST.get("content")
    raw_user_id = request.POST.get("user_id")    # "None" などの文字が来る可能性
    if not content:
        return JsonResponse({"error": "content is required"}, status=400)

    # 質問チェック
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        return JsonResponse({"error": "Question not found"}, status=404)

    # user_idを安全に変換
    user = None
    if raw_user_id not in [None, "", "None", "null"]:
        try:
            user_id = int(raw_user_id)
            user = Users.objects.get(id=user_id)
        except:
            user = None  # 取れなければ匿名回答

    answer = Answers.objects.create(
        question=question,
        user=user,
        content=content,
    )

    return redirect(f'/inquiry/{question_id}/')


def answer_form_page(request, question_id):
    """回答フォームページの表示"""
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        return render(request, "errors/404.html", status=404)

    # 回答一覧
    answer_list = [{
        "id": a.id,
        "user": str(a.user.name) if a.user else None,
        "content": a.content,
        "created_at": a.created_at,
    } for a in question.answers.all()]

    if question.user:
        data = {
            "id": question.id,
            "title": question.title,
            "user_name": question.user.name,
            "team_name": question.team_name,
            "category": question.category,
            "content": question.content,
            "is_answer": question.is_answer,
            "created_at": question.created_at,
            "updated_at": question.updated_at,
            "answers": answer_list,
        }
    else:
        data = {
            "id": question.id,
            "title": question.title,
            "user_name": None,
            "team_name": question.team_name,
            "category": question.category,
            "content": question.content,
            "is_answer": question.is_answer,
            "created_at": question.created_at,
            "updated_at": question.updated_at,
            "answers": answer_list,
        }

    return render(request, "answers/index.html", {"question": data})