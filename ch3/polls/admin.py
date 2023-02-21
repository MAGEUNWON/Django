from django.contrib import admin
from polls.models import Question, Choice

# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)

# models.py 모듈에서 정의한 Question, Choice 클래스를 임포트하고, admin.site.register() 함수를 사용하여 임포트한 클래스를 Admin 사이트에 등록해주면 됨. 이 처럼 테이블을 새로 만들 때는 models.py와 admin.py 두 개의 파일을 함께 수정해야 함
