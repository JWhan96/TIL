from django.db import models

# Create your models here.
# 상속(models 모듈.Model클래스)
# 작성한 모델 클래스는 DB에 생성될 테이블 구조 만드는 것
class Article(models.Model):
    # 클래스 변수
    title = models.CharField(max_length=10) #클래스
    # 클래스 변수
    content = models.TextField() #클래스
    # 생성일
    created_at = models.DateTimeField(auto_now_add=True)
    # 업데이트 날짜
    updated_at = models.DateTimeField(auto_now=True)


    