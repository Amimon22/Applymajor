from django.urls import path
from . import views
from .views import change_password
from .views import user_logout, logout_success


urlpatterns = [
    path('login/', views.user, name='login'),  # 로그인 페이지 URL 
    path('register/', views.register, name='register'),  # 회원가입 페이지 URL 
    path('accounts/change_password/', change_password, name='change_password'),  #비밀번호 재설정 페이지 URL 
    path('login/success/', views.login_success, name='success'),
    path('logout/', user_logout, name='logout'),
    path('logout/success/', logout_success, name='logout_success'),
]
