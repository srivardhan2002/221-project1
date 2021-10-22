from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("lib_login/", views.lib_login, name = "lib_login"),
    path('stu_login/', views.stu_login, name = "stu_login"),
    path('lib/', views.lib, name = "lib"),
    path('stu/', views.stu, name = "stu"),
    path('add/<str:un>', views.add, name = "add"),
    path('add2/<str:un>', views.add2, name = "add2"),
]