from django.db import models
from django.contrib.auth.models import User

class calculator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    subject = models.BooleanField(default=False) #전공탐색과목 이수 여부
    delight = models.IntegerField() #비교과활동점수
    professor1 = models.BooleanField(default=False) #1학기 지도교수상담
    professor2 = models.BooleanField(default=False) #2학기 지도교수상담
    course = models.IntegerField() #이수학점
    grade = models.FloatField() #평균학점
    result = models.FloatField(default = 0) #계산 결과