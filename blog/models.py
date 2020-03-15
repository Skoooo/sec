from django.conf import settings
from django.db import models
from django.utils import timezone

# 모델 필드 관련 링크 : https://docs.djangoproject.com/en/2.0/ref/models/fields/#field-types

class Post(models.Model): # Post : 모델이름 models : 장고모델임을 의미(데이터베이스에 저장됨)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #다른 모델 링크
    title = models.CharField(max_length=200) # 글자수 제한 O 텍스트 정의, 글제목
    text = models.TextField() # 글자수 제한 X 텍스트 정의, 글내용
    created_date = models.DateTimeField( #날자와 시간
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self): # 입력받는 메서드
        self.published_date = timezone.now()
        self.save()

    def __str__(self): # Post 모델의 제목 텍스트 반환
        return self.title

# 모델 장고 모델에 반영(콘솔창에 python manage.py makemigrations blog)
# 데이터베이스에 반영(python manage.py migrate blog)