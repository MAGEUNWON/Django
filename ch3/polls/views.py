# 장고의 단축함수인 render() 함수를 임포트함
from django.shortcuts import get_object_or_404, render
# vote 뷰에서는 리다이렉트 기능이 필요함. 이를 위해 HttpResonseRedirect 클래스를 임포트함
from django.http import HttpResponseRedirect
# url 처리를 위해 reverse() 함수를 임포트함
from django.urls import reverse
# Question 테이블에 엑세스하기 위해 polls.models.Question 클래스를 임포트
from polls.models import Choice, Question

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

# 뷰 함수를 정의. request 객체는 필수 인자. detail() 뷰처럼 question_id 인자를 더 받음.
# path('polls/<int:question_id>/vote/', views.vote, name='vote'), ->(urls.py에 있음) 에 의해 vote() 뷰 함수로 인자가 넘어옴


def vote(request, question_id):
    # get_object_or_404() 단축함수 사용
    question = get_object_or_404(Question, pk=question_id)
    try:  # Choice 테이블을 검색. 검색 조건은 pk=request.POST['choice']임. request.POST는 제출된 폼의 데이터를 담고있는 객체로서, 파이썬 사전처럼 키로 그 값을 구할 수 있음. request.POST['choice']는 폼 데이터에서 키가 'choice'에 해당하는 값인 choice.id를 스트링으로 리턴함
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # 폼의 POST 데이터에서 'choice'라는 키가 없으면 KeyError 익셉션을 발생시킴. 또는 검색 조건에 맞는 객체가 없으면 Choice.DoesNotExist 익셉셥이 발생
    except (KeyError, Choice.DoesNotExist):
        # 익셉션이 발생하면 render() 함수에 의해서 question과 error_message 컨텍스트 변수를 detail.html 템플릿으로 전달함. 사용자에게 에러메시지와 함께 설문 투표 폼을 다시 보여줌.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice."
        })
    else:  # 익셉션이 발생하지 않고 정상 처리 하는 경우
        selected_choice.votes += 1  # Choice 객체.votes 속성 즉, 선택 카운트를 +1 증가시킴
        selected_choice.save()  # 변경 사항을 해당 Choice 테이블에 저장함.
        # POST 데이터를 정상적으로 처리하였으면,
        # 항상 HttpResponseRedirect를 반환하여 리다이렉션 처리함
        # 이번에 vote()뷰 함수가 반환하는 객체는 HttpResponse가 아니라 HttpResponseRedirect 객체임. 리다이렉트할 타겟 URL을 인자로 받음. 타겟 URL은 reverse() 함수로 만듬.
        return HttpResponseRedirect(reverse('polls:results', args=(question_id,)))
        # 최종적으로 vote()뷰 함수는 리다이렉트할 타겟 URL을 담은 HttpResponseRedirect 객체를 반환함. 이처럼 웹프로그램에서 POST 방식의 폼 데이터를 처리하는 경우, 그 결과를 보여줄 수 있는 페이지로 이동시키기 위해 HttpResponseRedirect 객체를 리턴하는 것이 일반적임.


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    # render 함수 사용. 템플릿으로 question 변수를 넘겨주는 것은 동일하지만 템플릿 파일이 다르므로, 사용자에게 보여주는 화면은 달라짐
    # results 뷰는 최종적으로 results.html 템플릿 코드를 렌더링한 결과인 HTML 텍스트 데이터를 담은 HttpResponse 객체를 반환함.
    return render(request, 'polls/results.html', {'question': question})
