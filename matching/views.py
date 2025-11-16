from django.shortcuts import render, redirect
from .models import StudyGroup  # 1. 모델 import
import json  # 2. JSON import


# 1. 스터디/공모전 '목록' 뷰
def study_list(request):
    # DB에서 '모집중'인 모든 그룹을 가져옵니다.
    groups_queryset = StudyGroup.objects.filter(is_recruiting=True).order_by('-created_at')

    # DB 데이터를 JavaScript가 쓸 수 있는 리스트(JSON)로 변환합니다.
    # (친구분의 'dummyUsers'와 똑같은 모양으로 만듭니다)
    groups_list = []
    for group in groups_queryset:
        groups_list.append({
            'name': group.title,  # DB의 title -> JS의 name
            'field': group.field,  # DB의 field -> JS의 field
            'intro': group.description,  # DB의 description -> JS의 intro
            'emoji': '👩‍💻' if group.category == 'study' else '💡',  # DB의 category -> JS의 emoji
            'contact': group.leader_contact  # DB의 leader_contact -> JS의 contact
        })

    # 4. 'context'에 JSON 문자열로 변환하여 전달
    context = {
        'study_groups_json': json.dumps(groups_list)
    }
    return render(request, 'matching/index.html', context)


# 2. 스터디/공모전 '등록' 뷰 (이게 꼭 있어야 합니다!)
def study_create(request):
    if request.method == 'POST':
        # 템플릿 <form>의 'name' 속성으로 데이터를 받음
        category = request.POST.get('input-emoji')  # 'study' 또는 'contest'
        title = request.POST.get('input-name')
        field = request.POST.get('input-field')
        description = request.POST.get('input-intro')
        leader_contact = request.POST.get('input-contact')

        # DB에 저장
        StudyGroup.objects.create(
            category=category,
            title=title,
            description=description,
            leader_contact=leader_contact,
            field=field
        )
        # 저장 후, 목록 페이지로 새로고침
        return redirect('study_list')

    # POST 방식이 아니면 그냥 목록 페이지로 보냄
    return redirect('study_list')