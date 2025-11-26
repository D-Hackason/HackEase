from django.urls import path
from . import views

urlpatterns = [
    # 回答フォーム（HTMLページ）
    path('<int:question_id>/form/', views.answer_form_page, name='answer_form'),

    # 回答POST用 API は別
    path('<int:question_id>/create/', views.create_answer, name='create_answer'),
]