from django.shortcuts import render
from django.http import HttpResponse
from .models import calculator

def calculator(request): 
    result = 0
    if (subject == 1):   #전탐과목 이수함(1)
        result +=  400
    
    result += delight   #비교과 점수 자체 추가

    if (professor1 == 1):   #1학기 지도교수 상담완료(1)
        result += 50
    
    if (professor2 == 1):   #2학기 지도교수 상담완료(1)
        result += 50

    if (course > 36):
        course = 36
    result += (course / 36 * 150)

    if (grade > 4.5):
        grade = 4.5
    result += (grade / 4.5 * 150)

    return render(request, 'calculator.html', {'result': result})   #계산 결과 나오는 html로 연결