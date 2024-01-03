# from django.db import models
# from django.contrib.auth.models import User

# class APIData(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE) #유저
#     Student_ID = models.IntegerField(default=0, **options) #학번
#     Aff_Department = models.CharField(max_length=100) #소속학부
#     Overall_Rating = models.FloatField(**options) #전체평점
#     Credit = models.IntegerField(default=0, **options) #이수학점
#     Subject = models.CharField(max_length=100)  #전공선택 수강과목은 여러개여서 배열,,,을 써야하는데 나중에 

# class Apply(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)   #유저 불러오기
#     department = models.CharField(max_length = 200)   #소속대학(과기대, 글융, 아앤디)
#     orderOfApplication1 = models.CharField(max_length = 200)   #1지망
#     orderOfApplication2 = models.CharField(max_length = 200)   #2지망
#     orderOfApplication3 = models.CharField(max_length = 200)   #3지망
#     orderOfApplication4 = models.CharField(max_length = 200)   #4지망