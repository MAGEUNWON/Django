# 장고의 단축함수인 render() 함수를 임포트함
from django.shortcuts import get_object_or_404, render
# Question 테이블에 엑세스하기 위해 polls.models.Question 클래스를 임포트
from polls.models import Question

# Create your views here.

# 뷰 함수를 정의함. request 객체는 뷰 함수의 필수 인자.


def index(request):
    # 템플릿에 넘겨줄 객체 이름은 latest_question_list임. latest_question_list 객체는 Question 테이블 객체에서 pup_data 컬럼의 역순으로 정렬하여 5개의 최근 Question 객체를 가져와서 만듬
    latest_question_list = Question.objects.all().order_by('-pub_data')[:5]
    # 템플릿에 넘겨주는 방식은 파이썬 사전 타입으로, 템플릿에 사용될 변수명과 그 변수명에 해당하는 객체를 매핑하는 사전으로 context 변수를 만들어서 이를 render() 함수에 보내 줌.
    context = {'latest_question_list': latest_question_list}
    # render() 함수는 템플릿 파일인 polls/index.html에 context 변수를 적용하여 사용자에게 보여줄 최종 HTML 텍스트를 만들고, 이를 담아서 HttpResponse 객체를 반환함
    # index() 뷰 함수는 최종적으로 클라이언트에게 응답할 데이터인 HttpResponse 객체를 반환함.
    return render(request, 'polls/index.html', context)

# 뷰 함수를 정의, request 객체는 필수 인자이고, 추가적으로 question_id 인자를 더 받음. 다음과 같이 정의한 URL 패턴으로부터 추출된 question_id 파라미터가 뷰 함수의 인자로 넘어 오는 것.


def detail(request, question_id):
    # get_object_or_404 단축함수 사용. 이 함수의 첫 번째 인자는 모델 클래스이고, 두 번째 인자부터는 검색 조건을 여러개 사용할 수 있음. 이 예제에서는 Question 모델 클래스로부터 pi=question_id 검색 조건에 맞는 객체를 조회, 조건에 맞는 객체가 없으면 Http404 익셉셥을 발생시킴
    question = get_object_or_404(Question, pk=question_id)
    # render 함수 다시 사용. 이는 템플릿 파일 polls/detail.html에 컨텍스트 변수를 적용하여 사용자에게 보여 줄 최종 HTML 텍스트를 만들고, 이를 담아서 HttpResponse 객체를 반환함. 템플릿에게 넘겨주는 컨텍스트 사전을 render() 함수의 인자로 직접 써주고 있음. 템플릿 파일에서는 question 이란 변수를 사용할 수 있게 됨.
    # detail() 뷰 함수는 최종적으로 detail.html의 텍스트 데이터를 담은 HttpResponse 객체를 반환
    return render(request, 'polls/detail.html', {'question': question})
