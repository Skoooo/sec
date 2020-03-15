from django.contrib import admin
from .models import Post # 모델에서 Post 불러옴

admin.site.register(Post) # 관리자 페이지에 모델 등록


#장고 관리자 관련 링크 : https://docs.djangoproject.com/en/2.0/ref/contrib/admin/