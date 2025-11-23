from django.urls import path
from . import views

app_name = "portral"
urlpatterns=[
    path("requirements/",views.list,name="list"),
    path("requirements/<int:id>",views.list_detail,name="list_detail"),
]