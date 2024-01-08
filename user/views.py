#로그인하는 
from django.contrib.auth import authenticate, login
#비밀번호 변경하는 기능 
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required #forms.py 파일 따로 안만들고 
from django.contrib.auth import update_session_auth_hash
# from apply.models import Application #이전기록 
from django.shortcuts import render

#회원가입하는 코드 
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

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


#여기서 비밀번호 서로 달라도 넘어가는데 그 이유는 회원가입 버튼을 눌러도 다음 페이지로 넘어가는 이유는 회원가입 버튼을 눌렀을 때, 서버 측에서 비밀번호 일치 여부를 확인하고 에러 메시지를 반환하고 있지만, 클라이언트 측에서 이 에러 메시지를 처리하고 다음 페이지로 넘어가도록 구현되어 있기 때문입니다.

# 클라이언트 측에서는 render 함수를 사용하여 서버로부터 받은 에러 메시지와 함께 회원가입 페이지를 다시 렌더링합니다. 그리고 이때, 입력한 비밀번호와 확인용 비밀번호가 일치하지 않는 경우에는 에러 메시지가 표시되도록 되어 있습니다. 그러나 클라이언트 측에서는 이 에러 메시지를 받아도 다음 페이지로 넘어가는 기능이 구현되어 있지 않아서, 실제로는 다음 페이지로 넘어가지 않아야 합니다.

# 따라서, 이 문제를 해결하기 위해서는 클라이언트 측에서 회원가입 버튼을 눌렀을 때, 비밀번호 일치 여부를 확인하고 다음 페이지로 넘어가지 않도록 JavaScript를 사용하여 처리해야 합니다. JavaScript를 사용하여 비밀번호 일치 여부를 확인하고, 일치하지 않는 경우에는 다음 페이지로 넘어가지 않도록 이벤트 핸들러를 제어하면 됩니다.

# JavaScript를 사용하는 방법에 대해서 자세히 설명드리려면, 프로젝트의 구조와 사용하는 JavaScript 라이브러리에 따라 달라질 수 있으므로, 구체적인 코드를 제공하기 어렵습니다. 그러나 JavaScript를 사용하여 비밀번호 일치 여부를 확인하고 다음 페이지로 넘어가지 않도록 구현하는 방법에 대해서는 다음과 같이 설명드릴 수 있습니다.

# HTML 폼에 비밀번호 확인 필드를 추가합니다. (예: <input type="password" name="confirm_password">)
# JavaScript를 사용하여 회원가입 버튼 클릭 시, 입력한 비밀번호와 확인용 비밀번호가 일치하는지 확인하는 함수를 작성합니다.
# 이 함수에서 비밀번호가 일치하지 않는 경우, 이벤트의 기본 동작을 중단시킵니다. (예: event.preventDefault())
# 일치하지 않는 경우, 에러 메시지를 표시하거나 다른 방법으로 사용자에게 알립니다.
# 위의 방법을 참고하여 JavaScript를 사용하여 비밀번호 일치 여부를 확인하고 다음 페이지로 넘어가지 않도록 구현해보시기 바랍니다. 추가적인 도움이 필요하시면 언제든지 말씀해주세요.
#라고함....
    
#로그인하는 코드 
def user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_home')  # 로그인 성공 시 리다이렉트할 URL
        else:
            error_message = '아이디 또는 비밀번호가 올바르지 않습니다.'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')

@login_required #로그인 상태여야함상태여야함
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # 세션의 인증 정보 업데이트
            return redirect('password_change_done')
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