from django.db import models


class StudyGroup(models.Model):
    # '스터디'인지 '공모전'인지 선택
    CATEGORY_CHOICES = [
        ('study', '스터디'),
        ('contest', '공모전'),
    ]

    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, verbose_name="카테고리")
    title = models.CharField(max_length=200, verbose_name="제목 (예: 장고 백엔드 스터디)")
    description = models.TextField(verbose_name="상세 내용")

    # (선택) User 모델을 아직 안 썼다면 간단히 CharField로 대체
    leader_contact = models.CharField(max_length=100, verbose_name="팀장 연락처 (이메일/카톡ID)")

    field = models.CharField(max_length=100, verbose_name="관심 분야", default="기타")

    is_recruiting = models.BooleanField(default=True, verbose_name="모집중")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.get_category_display()}] {self.title}"
