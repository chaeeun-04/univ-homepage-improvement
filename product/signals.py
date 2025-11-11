from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Post  # product 앱의 Post 모델
from notifications.models import KeywordAlert  # 1단계의 KeywordAlert 모델


# Post 모델이 저장(save)된 후(post)에 이 함수를 실행
@receiver(post_save, sender=Post)
def check_post_for_keywords(sender, instance, created, **kwargs):
    # 'created'가 True일 때만 실행 (즉, 새 글이 작성되었을 때만)
    if created:
        post = instance
        # 검색 대상이 될 본문 (제목 + 내용)
        content = (post.title + " " + (post.content or "")).lower()

        # DB에 저장된 모든 알림 설정을 가져옴
        all_alerts = KeywordAlert.objects.all()

        # {email: [keyword1, keyword2]} 형태의 딕셔너리
        alerts_to_send = {}

        # 모든 알림 설정을 순회하며 키워드 검사
        for alert in all_alerts:
            if alert.keyword.lower() in content:
                # 키워드가 포함되어 있다면, 이메일 주소를 키로 목록에 추가
                if alert.email not in alerts_to_send:
                    alerts_to_send[alert.email] = []
                alerts_to_send[alert.email].append(alert.keyword)

        # [ 중요! ] 알림 대상이 있으면 터미널(콘솔)에 print 실행
        # (이 코드는 get_absolute_url을 호출하지 않습니다)
        if alerts_to_send:
            print("\n" + "=" * 50)
            print(f"[키워드 알림] 새 글 감지! (제목: {post.title})")

            for email, keywords in alerts_to_send.items():
                print(f"  -> 알림 대상: {email}")
                print(f"  -> 감지된 키워드: {', '.join(keywords)}")

            print("=" * 50 + "\n")