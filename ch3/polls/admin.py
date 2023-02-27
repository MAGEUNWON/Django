from django.contrib import admin
from polls.models import Question, Choice

# Register your models here.


# extra 변수로 지정한 값에 따라, 한 번에 보여주는 Choice text의 숫자가 결정됨. 2개의 항목을 추가로 입력할 수 있음.
# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 2

class ChoiceInline(admin.TabularInline):  # 테이블 형식으로 보여주기
    model = Choice
    extra = 2

# class QuestionAdmin(admin.ModelAdmin):
#     fields = ['pub_data', 'question_text']  # 필드 순서 변경


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question Statement', {'fields': ['question_text']}),
        ('Data Information', {'fields': [
         'pub_data'], 'classes': ['collapse']}), # 필드 접기 기능
    ]
    inlines = [ChoiceInline]  # Choice 모델 클래스 같이 보기
    list_display = ('question_text', 'pub_data')  # 레코드 리스트 컬럼 항목 지정
    list_filter = ['pub_data']  # 필터 사이드 바 추가
    search_fields = ['question_text']  # 검색 박스 추가


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)

# models.py 모듈에서 정의한 Question, Choice 클래스를 임포트하고, admin.site.register() 함수를 사용하여 임포트한 클래스를 Admin 사이트에 등록해주면 됨. 이 처럼 테이블을 새로 만들 때는 models.py와 admin.py 두 개의 파일을 함께 수정해야 함
