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

    def get_1st_priority_choices(self):
        return self.choice_set.filter(priority=1)

    def get_1st_priority_rank(self, support_model):
        choices = self.get_1st_priority_choices().filter(major=support_model)
        rank = choices.order_by('priority').first()

        return rank.priority if rank else None
    
    def calculate_competition_rate(self, major):
        total_users = User_apply_profile.objects.filter(major_choices=major).count()

        major_capacity = major.maximum if major.maximum is not None else 0

        competition_rate = (total_users / major_capacity) * 100 if major_capacity != 0 else 0
        
        return competition_rate

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
