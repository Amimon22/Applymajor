from django.db import models
from django.contrib.auth.models import User

class Apply(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)   #유저 불러오기
    department = models.CharField(max_length = 200)   #소속대학(과기대, 글융, 아앤디)
    orderOfApplication1 = models.CharField(max_length = 200)   #1지망
    orderOfApplication2 = models.CharField(max_length = 200)   #2지망
    orderOfApplication3 = models.CharField(max_length = 200)   #3지망
    orderOfApplication4 = models.CharField(max_length = 200)   #4지망