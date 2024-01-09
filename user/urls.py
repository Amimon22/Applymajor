from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.user, name='login'),  # 로그인 페이지 URL 
    path('register/', views.register, name='register'),  # 회원가입 페이지 URL 
    path('change_password/', views.change_password, name='change_password'),  #비밀번호 재설정 페이지 URL 
]
