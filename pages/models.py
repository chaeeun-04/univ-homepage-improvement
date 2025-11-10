from django.db import models

class MenuClick(models.Model):
    # 메뉴를 식별할 고유한 이름 (예: 'timetable', 'graduation')
    menu_name = models.CharField(max_length=50, unique=True, primary_key=True)
    # 화면에 표시될 이름 (예: '종합강의시간표')
    display_name = models.CharField(max_length=100)
    # 최종적으로 이동할 URL의 이름 (urls.py에 정의된 name)
    target_url_name = models.CharField(max_length=100)
    # 클릭 횟수
    click_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.display_name} ({self.click_count} clicks)"