from django.contrib import admin
from .models import MenuClick # MenuClick 모델을 import

# admin 사이트에 MenuClick 모델을 등록
admin.site.register(MenuClick)
