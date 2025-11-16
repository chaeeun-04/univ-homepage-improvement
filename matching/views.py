from django.shortcuts import render, redirect
from .models import StudyGroup  # [수정!] 'MatchCard'가 아니라 'StudyGroup'을 import
import json


# 1. 스터디/공모전 '목록' 뷰
def study_list(request):
    # [수정!] 'StudyGroup' 모델 사용
    groups_queryset = StudyGroup.objects.filter(is_recruiting=True).order_by('-created_at')

    groups_list = []
    for group in groups_queryset:
        groups_list.append({
            'name': group.title,
            'field': group.field,
            'intro': group.description,
            'emoji': '👩‍💻' if group.category == 'study' else '💡',
            'contact': group.leader_contact
        })

    context = {
        'study_groups_json': json.dumps(groups_list)
    }

    return render(request, 'matching/index.html', context)


# 2. 스터디/공모전 '등록' 뷰
def study_create(request):
    if request.method == 'POST':
        category = request.POST.get('input-emoji')
        title = request.POST.get('input-name')
        field = request.POST.get('input-field')
        description = request.POST.get('input-intro')
        leader_contact = request.POST.get('input-contact')

        # [수정!] 'StudyGroup' 모델 사용
        StudyGroup.objects.create(
            category=category,
            title=title,
            description=description,
            leader_contact=leader_contact,
            field=field
        )
        return redirect('study_list')

    return redirect('study_list')