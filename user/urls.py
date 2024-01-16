from django.urls import path
from .views import user, register, user_logout, logout_success,change_password, mypage, mypage_view


urlpatterns = [
    path('login/', user, name='login'),  # 로그인 페이지 URL 
    #path('login/success/', views.login_success, name='success'),
    path('register/', register, name='register'),  # 회원가입 페이지 URL 
    path('accounts/change_password/', change_password, name='change_password'),  #비밀번호 재설정 페이지 URL 
    path('logout/', user_logout, name='logout'),
    path('logout/success/', logout_success, name='logout_success'),
    path('mypage/', mypage, name = 'mypage'),
    path('mypage_view/', mypage_view, name = 'mypage_view'),
]
