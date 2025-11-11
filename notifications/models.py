from django.db import models


class KeywordAlert(models.Model):
    email = models.EmailField(verbose_name="알림 받을 이메일")
    keyword = models.CharField(max_length=100, verbose_name="키워드")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"[{self.keyword}] -> {self.email}"

    class Meta:
        # 한 사람이 같은 키워드를 중복 구독하는 것을 방지
        unique_together = ('email', 'keyword')
