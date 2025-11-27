from django.urls import path
from . import views

app_name = "inquiry" 

urlpatterns = [
    path('create/', views.question_form, name='question_form'),
    path("success/", views.success, name="success"),
    path('', views.question_list, name='question_list'),
    path('<int:question_id>/', views.question_detail, name='question_detail'),
]