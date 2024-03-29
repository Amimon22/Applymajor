from django.db import models
from django.contrib.auth.models import User




class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.IntegerField() #ID(학번) (정수형으로)
    password = models.CharField(max_length=50) #비밀번호 (문자열로)
    certification = models.BooleanField(default=False) #인증여부 (불리언으로)
    

# # Create your models here.
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     auth = models.BooleanField(default=False) #인증 완료된 유저 구분
