from django.db import models
from django.contrib.auth.models import User

user = models.OneToOneField(User, on_delete=models.CASCADE)

class APIData(models,Model):
    User = models.CharField(max_length=100) #유저
    Student_ID = models.IntegerField(default=0, **options) #학번
    Aff_Department = models.CharField(max_length=100) #소속학부
    Overall_Rating = models.FloatField(**options) #전체평점
    Credit = models.IntegerField(default=0, **options) #이수학점
    Subject = models.CharField(max_length=100)  #전공선택 수강과목은 여러개여서 배열,,,을 써야하는데 나중에 

# Create your models here.
class Startpage(models.Model):
    def __str__(self):
        return self.name