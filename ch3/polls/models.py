from django.db import models

# Create your models here.


# 장고에서는 테이블을 하나의 클래스로 정의하고, 테이블의 컬럼은 클래스의 변수(속성)로 매핑함. 테이블 클래스는 django.db.odels.Model클래스를 상속받아 정의하고, 각 클래스 변수의 타입도 장고에서 미리 정의된 필드 클래스를 사용

# PK(Primary Key)는 클래스에 지정해 주지 않아도, 장고는 항상 PK에 대한 속성을 Not Null 및 Autoincrement로, 이름은 id로 해서 자동으로 만들어 줌
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    # DateTimeField() 클래스에 정의한 date published는 put_data 컬럼에 대한 레이블 문구. Admin 사이트에서 이 문구를 보게 될 것
    pub_data = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    # FK(Foreign Key)는 항상 다른 테이블의 PK에 연결되므로, Question 클래스의 id 변수까지 지어할 필요 없이 Question 클래스만 지정하면 됨. 실제 테이블에서 FK로 지정된 컬럼은 _id 접미사가 붙음
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

# __str__()메소드는 객체를 문자열로 표현할 때 사용하는 함수. Admin 사이트나 장고 쉘 등에서 테이블명을 보여 줄 때, 이때 __str__() 메소드를 정의하지 않으면 테이블명이 제대로 표시되지 않음. 참고로 파이썬2에서는 __unicode__() 메소드를 사용
# models.py 파일에서 정의한 테이블을 admin.py 파일에 등록해야 Admin 사이트에 보임.
