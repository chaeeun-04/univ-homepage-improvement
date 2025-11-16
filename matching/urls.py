from django.urls import path
from . import views

urlpatterns = [
    # 1. /matching/ (메인 카드 UI)
    path('', views.study_list, name='study_list'),

    # 2. /matching/create/ (등록 폼이 보낼 곳)
    path('create/', views.study_create, name='study_create'),
]