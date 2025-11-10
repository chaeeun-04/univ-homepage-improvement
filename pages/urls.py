from django.urls import path
from . import views

urlpatterns = [
    # ... 기존 index 등 ...
    path('', views.index, name='index'),

    # --- 1. 최종 목적지 페이지들 ---
    # (3단계에서 Target_url_name에 사용한 이름과 'name='을 일치시켜야 함)
    path('timetable/', views.timetable_view, name='master_timetable'),
    path('graduation/', views.graduation_view, name='graduation_requirements'),
    path('forms/', views.forms_view, name='forms_archive'),
    path('cafeteria/', views.cafeteria_view, name='cafeteria_menu'),

    # --- 2. 클릭 추적용 URL ---
    # (예: /track/timetable/ 로 접속하면 track_menu_click 함수가 실행됨)
    path('track/<str:menu_name_pk>/', views.track_menu_click, name='track_click'),
]