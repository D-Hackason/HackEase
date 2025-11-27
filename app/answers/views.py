from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Answers
from inquiry.models import Question
from accounts.models import Users
from django.shortcuts import render

import json

@csrf_exempt
def create_answer(request, question_id):
    if request.method != "POST":
        return JsonResponse({"error": "POST only"}, status=400)

    try:
        data = json.loads(request.body)
    except:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    content = data.get("content")
    raw_user_id = data.get("user_id")    # "None" などの文字が来る可能性

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

    return JsonResponse({
            "message": "Answer created",
            "answer_id": answer.id
        }, json_dumps_params={'ensure_ascii': False})


def answer_form_page(request, question_id):
    """回答フォームページの表示"""
    try:
        question = Question.objects.get(id=question_id)
    except Question.DoesNotExist:
        return render(request, "errors/404.html", status=404)

    return render(request, "answers/answer_form.html", {
        "question_id": question_id,
        "question": question,  # タイトルなどテンプレ表示にも使える
        "user_id": request.user.id if request.user.is_authenticated else None,
    })