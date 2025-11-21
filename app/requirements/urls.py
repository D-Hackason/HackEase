from django.urls import path
from . import views
app_name = "requirements"
urlpatterns=[
    path("form/",views.form,name="form"),
    path("list/",views.list,name="list"),
    path("list/<int:id>",views.list_detail,name="list_detail"),
]