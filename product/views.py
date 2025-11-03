print("===== product/views.py 파일을 읽었습니다! =====")
from django.shortcuts import render
from .models import MainContent
from .models import Notice, Event
from django.db.models import Q

def index(request):
    print("===== index 페이지가 로드되었습니다! =====")
    content_list = MainContent.objects.all()
    context = {'content_list': content_list}
    return render(request, 'product/content_list.html', context)


def search_results(request):
    print("--- 1. 검색 요청 받음 ---")

    query = request.GET.get('q')
    all_results = []

    if query:
        print(f"--- 2. 검색어 '{query}' 확인 ---")

        notice_results = Notice.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

        event_results = Event.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )

        print("--- 3. DB 쿼리 준비 완료 (아직 실행 전) ---")

        for notice in notice_results:
            all_results.append({
                'type': '공지사항',
                'title': notice.title,
                'url': '#'
            })

        print("--- 4. Notice 모델 검색 완료 ---")

        for event in event_results:
            all_results.append({
                'type': '행사',
                'title': event.name,
                'url': '#'
            })

        print("--- 5. Event 모델 검색 완료 ---")

    else:
        query = ""
        print("--- 2. 검색어 없음 ---")

    context = {
        'query': query,
        'results': all_results,
    }

    print("--- 6. 템플릿 렌더링 시작 ---")

    response = render(request, 'product/search_results.html', context)

    print("--- 7. 렌더링 완료. 응답 보냄 ---")

    return response