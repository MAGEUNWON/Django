"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# 필요한 모듈과 함수를 임포트함. admin 모듈과 path() 함수는 장고에서 제공하는것.
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls'))
]

# URL/뷰 매핑을 정의하는 방식은 항상 동일하므로, 그대로 코딩하면 됨. URL 패턴 매칭은 위에서 아래로 진행하므로 정의하는 순서에 유의.
# urlpatterns = [
#     # 장고의 Admin 사이트에 대한 URLconf는 이미 정의되어 있음. 이를 활욯하고 있는 것. Admin 사이트를 사용하기 위해서는 항상 이런식으로 정의함.
#     path('admin/', admin.site.urls),
#     # polls 애플리케이션에 대한 URL/뷰 매핑을 정의.
#     path('polls/', views.index, name='index'),
#     path('polls/<int:question_id>/', views.detail, name='detail'),
#     path('polls/<int:question_id>/results/', views.results, name='result'),
#     path('polls/<int:question_id>/vote/', views.vote, name='vote'),
# ]
# 파일 두개로 분리함. polls>urls.py로 하나 더 만듬

# path() 함수는 route, view 2개의 필수 인자와 kwargs, name 2개의 선택 인자를 받음
# route : URL 패턴을 표현하는 문자열. URL 스트링이라고도 부름
# view : URL 스트링이 매칭되면 호출되는 뷰 함수. HttpRequest 객체와 URL 스트링에서 추출된 항목이 뷰 함수의 인자로 전달.
# kwargs : URL 스트링에서 추출된 항목 외에 추가적인 인자를 뷰 함수에 전달할 때, 파이썬 사전 타입으로 인자를 정의함.
# name : 각 URL 패턴별로 이름을 붙여 줌. 여기서 정해준 이름은 주로 템플릿 파일에서 사용
