from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required #forms.py 파일 따로 안만들고 
from django.contrib.auth import update_session_auth_hash, authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import UserProfile
from apply.models import User_apply_profile


#회원가입 코드

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']  # 추가된 코드: 확인용 비밀번호

        # 비밀번호 확인 체크
        if password != confirm_password:
            error_message = '비밀번호가 일치하지 않습니다.'
            return render(request, 'register.html', {'error_message': error_message})

        # 아이디 중복 체크
        if User.objects.filter(username=username).exists():
            error_message = '이미 사용 중인 아이디입니다.'
            return render(request, 'register.html', {'error_message': error_message})
        else:
            # 회원 생성
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect('login')  # 회원가입 성공 시 로그인 페이지로 리다이렉트
    else:
        return render(request, 'register.html')

#로그인 코드 
def user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('success')  # 로그인 성공 시 리다이렉트할 URL
        else:
            error_message = '아이디 또는 비밀번호가 올바르지 않습니다.'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

#로그인 성공 페이지로 가기위함
def login_success(request):
    return render(request, 'login_success.html')


#비밀번호 변경 코드
@login_required #로그인 상태여야함상태여야함
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            print(f"비밀번호가 변경된 사용자: {user}")
            update_session_auth_hash(request, user)  # 세션의 인증 정보 업데이트
            print("비밀번호 변경완료")           
            return redirect('password_change_done')
        else:
            print(f"폼 에러: {form.errors}")
    else:
        form = PasswordChangeForm(request.user)
    
    return render(request, 'change_password.html', {'form': form})


# def user_detail(request):
#     users = User.objects.all()
#     return render(request, 'user_detail.html', {'users': users})

#이전기록 가져오는 기능

# def user_history(request):
#     # 현재 로그인한 사용자의 이전 지원 기록을 가져옵니다.
#     history = Application.objects.filter(user=request.user)
    
#     return render(request, 'user_history.html', {'history': history})

#프론트엔드 파일 렌더링하는 코드 
# def index(request):
#     return render(request, '프론트엔드_파일_경로/index.html')


#로그아웃 코드

def user_logout(request):
    if request.method == 'POST':
        logout(request)
        return redirect('logout_success')
    return render(request, 'logout.html')

#로그아웃 성공한 페이지로 가기위함 
def logout_success(request):
    return render(request, 'logout_success.html')

#마이페이지 
@login_required  # 로그인한 사용자만 접근 가능하도록 설정
def mypage(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'mypage.html', {'user_profile' : user_profile})

#apply에 models.py에 있는 User_apply_profile 클래스 데이터 가져오기 
def mypage_view(request):
    #User_apply_profile 데이터 가져오기
    apply_data = User_apply_profile.objects.all()  # 또는 필요한 쿼리를 사용하여 데이터를 가져옴
    return render(request, 'user/mypage.html', {'apply_data': apply_data})