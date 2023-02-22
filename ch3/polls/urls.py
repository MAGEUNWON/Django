from django.urls import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),  # /polls/
    path('<int:question_id>/', views.detail, name='detail'),  # /polls/5/
    path('<int:question_id>/results/', views.results,
         name='results'),  # /polls/5/results
    path('<int:question_id>/vote/', views.vote, name='vote'),  # /polls/5/vote
]


# polls/urls.py 파일에서 사용한 app_name 변수는 URL 패턴의 이름이 충돌나는 것을 방지하기 위한 이름공간의 역할을 함. 보통 프로젝트에서 여러 개의 애플리케이션으로 이뤄짐. 예를 들어 polls 애플리케이션의 URL 패턴 이름과 blog 애플리케이션의 URL 패턴 이름이 모두 detail이 되는 경우가 발생할 수 있음. 이 둘을 구별하기 위해 app_name 변수로 이름 공간을 지정하는 것. 즉 polls 애플리케이션의 detail은 polls:detail, blog 애플리케이션의 detail은 blog:detail로 표기해서 구분
