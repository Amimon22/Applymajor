from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Source(models.Model):
    src_file = models.CharField(max_length=225, default='')
    src_name = models.CharField(max_length=225, default='')
    src_link = models.CharField(max_length=225, default='')
    result_text = models.CharField(max_length=4096, default='')
    status = models.CharField(max_length=10, default='')
    usage_flag = models.CharField(max_length=10, default='')
    create_at = models.DateTimeField()

class Academic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student_number = models.CharField(max_length=20, default='')
    academic_status = models.CharField(max_length=50, default='') 
    grade = models.IntegerField()
    major = models.CharField(max_length=50, default='')

    def __str__(self):
        return f"{self.user.username}'s Academic Info"
    
class Apply(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)   #유저 불러오기
    first_choice = models.CharField(max_length = 200)   #1지망
    second_choice = models.CharField(max_length = 200)   #2지망
    third_choice = models.CharField(max_length = 200)   #3지망
    fourth_choice = models.CharField(max_length = 200)   #4지망
    
class Departure_Major_Code(models.Model):
    departments_majors_codes = {
        '글로벌융합대학' : {
            '국어국문학전공' : {
                '전탐과목코드' : '502241',
                '정원' : 35
            },
            '일어일문학전공' : {
                '전탐과목코드' : ['502242', '502243'],
                '정원' : 37
            },
            '중어중문학전공' : {
                '전탐과목코드' : ['502388', '502387'],
                '정원' : 46
            },
            '영어영문학전공' : {
                '전탐과목코드' : ['502245', '502246'],
                '정원' : 42
            },
            '불어불문학전공' : {
                '전탐과목코드' : ['502247', '502248'],
                '정원': 18
            },
            '독어독문학전공' : {
                '전탐과목코드' : ['502249', '502407'],
                '정원': 18
            },
            '스페인어전공' : {
                '전탐과목코드' : '502251',
                '정원' : 17
            },
            '사학전공' : {
                '전탐과목코드' : ['502252', '502253'],
                '정원' : 18
            },
            '철학전공' : {
                '전탐과목코드' : ['502254', '502255'],
                '정원' : 18
            },
            '미술사학전공' : {
                '전탐과목코드' : ['502257', '502256'],
                '정원': 25
            },
            '문화인류학전공' : {
                '전탐과목코드' : '502258',
                '정원' : 19
            },
            '경영학전공' : {
                '전탐과목코드' : ['502259', '502260'],
                '정원' :40
            },
            '회계학전공' : {
                '전탐과목코드' : '502831',
                '정원' : 39
            },
            '국제통상학전공' : {
                '전탐과목코드' : '502263',
                '정원' : 41
            },
            '법학전공' : {
                '전탐과목코드' : '502264',
                '정원' : 26
            },
            '사회학전공' : {
                '전탐과목코드' : ['502265', '502266'],
                '정원' : 18
            },
            '문헌정보학전공' : {
                '전탐과목코드' : '502267',
                '정원' : 30
            },
            '심리학전공' : {
                '전탐과목코드' : '502268',
                '정원' : 48
            },
            '아동가족학전공' : {
                '전탐과목코드' : ['502269', '502270'],
                '정원' : 20
            },
            '사회복지학전공' : {
                '전탐과목코드' : '502271',
                '정원' : 31
            },
            '정치외교학전공' : {
                '전탐과목코드' : '502272',
                '정원' : 30
            },
            '의상디자인전공' : {
                '전탐과목코드' : ['502273', '502274'],
                '정원' : 39
            }
        },

        '과학기술대학' : {
            '바이오공학전공' : {
                '전탐과목코드' : ['502289', '502290'],
                '정원' : 32
            },
            '디지털소프트웨어전공' : {
                '전탐과목코드' : ['502878', '502927', '502854'],
                '정원' : 142
            },
            '수학전공' : {
                '전탐과목코드' : ['502275'],
                '정원' : 36
            },
            '정보통계학전공' : {
                '전탐과목코드' : '502276',
                '정원' : 36
            },
            '화학전공' : {
                '전탐과목코드' : ['502277', '502278'],
                '정원' : 36
            },
            '식품영양학전공' : {
                '전탐과목코드' : ['502279', '502280'],
                '정원' : 58
            },
            '생활체육학전공' : {
                '전탐과목코드' : ['502832', '502281'],
                '정원' : 25
            }
        },

        'Art&Design대학' : {
            '동양화전공' : {
                '전탐과목코드' : ['502291', '502292'],
                '정원' : 18
            },
            '서양화전공' : {
                '전탐과목코드' : ['502293', '502294'],
                '정원' : 19
            },
            '실내디자인전공' : {
                '전탐과목코드' : ['502295', '502296'],
                '정원' : 20
            },
            '시각디자인전공' : {
                '전탐과목코드' : ['502297', '502298'],
                '정원' : 20
            },
            '텍스타일디자인전공' : {
                '전탐과목코드' : ['502299', '502300'],
                '정원' : 19
            }
        }
    }