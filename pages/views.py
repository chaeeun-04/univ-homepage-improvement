from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db.models import F
from .models import MenuClick


def track_menu_click(request, menu_name_pk):
    menu_item = get_object_or_404(MenuClick, pk=menu_name_pk)

    menu_item.click_count = F('click_count') + 1
    menu_item.save()

    target_url = reverse(menu_item.target_url_name)
    return redirect(target_url)


def index(request):
    top_2_menus = MenuClick.objects.order_by('-click_count')[:2]

    context = {
        'top_menus': top_2_menus
    }

    return render(request, 'pages/index.html', context)

def timetable_view(request):
    return render(request, 'pages/timetable.html') # 템플릿 이름은 원하는대로 수정 가능

def graduation_view(request):
    return render(request, 'pages/graduation.html')

def forms_view(request):
    return render(request, 'pages/forms.html')

def cafeteria_view(request):
    return render(request, 'pages/cafeteria.html')