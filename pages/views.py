from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db.models import F  # F() 표현식 import
from .models import MenuClick  # MenuClick 모델 import


def track_menu_click(request, menu_name_pk):
    # 1. DB에서 menu_name(PK)으로 해당 객체를 찾음 (없으면 404 에러)
    menu_item = get_object_or_404(MenuClick, pk=menu_name_pk)

    # 2. 클릭 횟수를 1 증가시킴 (F()는 경쟁 상태(Race Condition)를 방지)
    menu_item.click_count = F('click_count') + 1
    menu_item.save()

    # 3. 객체가 가진 'target_url_name'을 바탕으로 실제 이동할 URL을 찾아서 리다이렉트
    #    (예: 'master_timetable' -> '/timetable/')
    target_url = reverse(menu_item.target_url_name)
    return redirect(target_url)


def index(request):
    # DB에서 클릭 횟수 상위 2개를 가져옵니다.
    top_2_menus = MenuClick.objects.order_by('-click_count')[:2]

    # index.html로 이 데이터를 전달합니다.
    context = {
        'top_menus': top_2_menus
    }

    # 'pages/index.html' 템플릿을 화면에 보여줍니다.
    return render(request, 'pages/index.html', context)

def timetable_view(request):
    # TODO: 종합강의시간표 페이지 로직
    # 지금은 임시 템플릿만 연결합니다.
    return render(request, 'pages/timetable.html') # 템플릿 이름은 원하는대로 수정 가능

def graduation_view(request):
    # TODO: 졸업요건 페이지 로직
    return render(request, 'pages/graduation.html')

def forms_view(request):
    # TODO: 서식자료실 페이지 로직
    return render(request, 'pages/forms.html')

def cafeteria_view(request):
    # TODO: 식당게시판 페이지 로직
    return render(request, 'pages/cafeteria.html')