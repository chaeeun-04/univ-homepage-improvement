print("===== product/views.py 파일을 읽었습니다! =====")
from django.shortcuts import render
from django.db.models import Q  # Q 객체를 임포트합니다. (검색 로직의 핵심)

# 'product_data.json'의 내용을 보니 모델 이름이 'MainContent'입니다.
from .models import MainContent


# from .models import Notice, Event # <-- 지금은 MainContent만 검색하므로 일단 주석 처리

def index(request):
    print("===== index 페이지가 로드되었습니다! =====")


    query = request.GET.get('q')

    content_list = MainContent.objects.order_by('-pub_date')

    if query:

        print(f"--- 2. 검색어 '{query}'로 MainContent 검색 시작 ---")
        content_list = content_list.filter(
            Q(title__icontains=query) |  # MainContent의 제목
            Q(content__icontains=query)  # MainContent의 내용
        ).distinct()  # 중복 결과 제거
    else:
        print("--- 2. 검색어 없음. 전체 목록 표시 ---")


    context = {
        'content_list': content_list,
        'query': query,  # 템플릿에 검색어를 넘겨주어 폼에 값을 유지
    }

    return render(request, 'product/content_list.html', context)