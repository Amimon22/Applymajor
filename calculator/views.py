from django.shortcuts import render
from django.http import HttpResponse
from .models import calculator

def calculator(request):

    calculator.subject = bool(int(request.POST.get('subject', 0)))
    calculator.delight = int(request.POST.get('delight', 0))
    calculator.professor1 = bool(int(request.POST.get('professor1', 0)))
    calculator.professor2 = bool(int(request.POST.get('professor2', 0)))
    calculator.course = int(request.POST.get('course', 0))
    calculator.grade = float(request.POST.get('grade', 0))

    calculator.result = 0

    if (calculator.subject == 1):   #전탐과목 이수함(1)
        calculator.result +=  400
        
    calculator.result += calculator.delight   #비교과 점수 자체 추가

    if (calculator.professor1 == 1):   #1학기 지도교수 상담완료(1)
        calculator.result += 50
        
    if (calculator.professor2 == 1):   #2학기 지도교수 상담완료(1)
        calculator.result += 50

    if (calculator.course > 36):
        calculator.course = 36
    calculator.result += (calculator.course / 36 * 150)

    if (calculator.grade > 4.5):
        calculator.grade = 4.5
    calculator.result += (calculator.grade / 4.5 * 150)
    calculator.result = round(calculator.result, 2)

    return render(request, 'calculator.html', {'result': calculator.result})   #계산 결과 나오는 html로 연결