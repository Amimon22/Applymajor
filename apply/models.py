from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Department(models.Model):
    department_name = models.CharField(max_length=50)

    def __str__(self):
        return self.department_name

class Subject_code(models.Model):
    code = models.CharField(max_length=10)
    major = models.ForeignKey('Major', on_delete=models.CASCADE, related_name='subject_codes')

    def __str__(self):
        return f'{self.major} - {self.code}'

class Major(models.Model):
    major_name = models.CharField(max_length=255)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name='major')
    maximum = models.PositiveIntegerField(null=True)
    current_applicants = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.major_name} ({self.department})'

class Source(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    src_file = models.CharField(max_length=225, default='')
    src_name = models.CharField(max_length=225, default='')
    src_link = models.CharField(max_length=225, default='')
    result_text = models.TextField(max_length=4096, default='')
    status = models.BooleanField(max_length=10, default=False)
    usage_flag = models.CharField(max_length=10, default='')
    create_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.src_name} - {self.user.username}"
    
class Academic(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    student_number = models.CharField(max_length=20, default='')
    academic_status = models.CharField(max_length=50, default='') 
    grade = models.CharField(max_length=20, default='')
    major = models.CharField(max_length=50, default='')

    def __str__(self):
        return f"{self.user.username}'s Academic Info"
    
    def get_related_majors(self):
        related_majors = []
        if '글로벌융합대학' in self.major:
            related_majors = ['국어국문학전공', '일어일문학전공', '중어중문학전공', '영어영문학전공', '불어불문학전공', '독어독문학전공', '스페인어전공', '사학전공', '철학전공', '미술사학전공', '문화인류학전공', '경영학전공', '회계학전공', '국제통상학전공', '법학전공', '사회학전공', '문헌정보학전공', '심리학전공', '아동가족학전공', '사회복지학전공', '정치외교학전공', '의상디자인전공']
        elif '과학기술대학' in self.major:
            related_majors = ['디지털소프트웨어전공', '바이오공학전공', '생활체육학전공', '식품영양학전공', '정보통계학전공', '화학전공', '수학전공']
        elif 'Art&Design대학' in self.major:
            related_majors = ['동양화전공', '서양화전공', '실내디자인전공', '시각디자인전공', '텍스타일디자인전공']

        return Major.objects.filter(major_name__in=related_majors)

    
class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_code = models.CharField(max_length=1000)
    course_name = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.user.username} - {self.course_code} - {self.course_name}"
    
class Grade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    grades1 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    grades2 = models.DecimalField(max_digits=6, decimal_places=5, null=True)
    course_credits1 = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(3),])
    course_credits2 = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(3),])
    

class User_apply_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    major_choices = models.ManyToManyField(Major, through='Choice')
    
    def get_username(self):
        return self.user.username

    def get_priorities(self):
        return self.choice_set.order_by('priority').values_list('major', flat=True)
    
    def get_1st_priority_choices(self):
        return self.choice_set.filter(priority=1)

    def get_1st_priority_rank(self, support_model):
        choices = self.get_1st_priority_choices().filter(major=support_model)
        rank = choices.order_by('priority').first()

        return rank.priority if rank else None
    
    def get_priority_rank(self, major, priority):
        """
        특정 전공과 우선순위에 해당하는 지망 순위를 반환합니다.
        """
        try:
            choice = self.choice_set.get(major=major, priority=priority)
            return choice.get_rank()
        except Choice.DoesNotExist:
            return None
    
    def calculate_competition_rate_for_priority(self, major, priority):
        major_capacity = major.maximum if major.maximum is not None else 0

        users_with_same_priority = User_apply_profile.objects.filter(
            major_choices=major,
            choice__priority=priority,
            choice__major=major
        ).count()

        competition_rate = (users_with_same_priority / major_capacity) * 100 if major_capacity != 0 else 0

        return competition_rate
    
    def calculate_competition_rates(self, major):
        competition_rates = {}
        for priority in range(1, 5):
            competition_rates[priority] = self.calculate_competition_rate_for_priority(major, priority)
        return competition_rates
        
class Choice(models.Model):
    PRIORITY_CHOICES = (
        (1, '1순위'),
        (2, '2순위'),
        (3, '3순위'),
        (4, '4순위'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_apply_profile = models.ForeignKey(User_apply_profile, on_delete=models.CASCADE)  # User_apply_profile 모델과의 외래키 추가
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    priority = models.PositiveIntegerField(choices=PRIORITY_CHOICES)

    class Meta:
        unique_together = ['user', 'priority']

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.major.current_applicants = self.user_apply_profile.major_choices.count()
        self.major.save()

    def get_rank(self):
        """
        현재 Choice의 우선순위를 반환합니다.
        """
        return self.priority

#이전에 선택한 지망 저장, 남은 변경가능 횟수 저장
class UserPriorChoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    major = models.ForeignKey('Major', on_delete=models.CASCADE)
    priority = models.PositiveIntegerField(choices=Choice.PRIORITY_CHOICES)
    change_count = models.PositiveIntegerField(default=3)  # 변경 가능 횟수
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.user.username} - {self.major} - Priority {self.priority}"