window.onload = function() {
    setTimeout(function() {
        document.querySelector('.memon').classList.add('slide-up');
        document.querySelector('.info-text').classList.add('slide-up');
    }, 1000);
    setTimeout(function() {
        document.querySelector('.memon_chat1').classList.add('fade-in');
    }, 2000);
    setTimeout(function() {
        document.querySelector('.user_chat1').classList.add('fade-in');
    }, 2500);
};

document.getElementById('studentID').addEventListener('keydown', function(e) {
    if (e.key === 'Enter') {  // 엔터 키를 눌렀을 때
        setTimeout(function() {
            document.querySelector('.memon_chat2').classList.add('fade-in');
        }, 500);  // .memon_chat2를 0.5초 후에 보이게 함

        setTimeout(function() {
            document.querySelector('.user_chat2').classList.add('fade-in');
        }, 1000);  // .user_chat2를 1초 후에 보이게 함
    }
});

document.getElementById('password').addEventListener('keyup', function(e) {
    if (e.key === 'Enter') {
        setTimeout(function() {
            document.querySelector('.memon_chat3').classList.add('fade-in');
        }, 500);  // .memon_chat3를 0.5초 후에 보이게 함

        setTimeout(function() {
            document.querySelector('.user_chat3').classList.add('fade-in');
        }, 1000);  // .user_chat3를 1초 후에 보이게 함
    }
});

document.getElementById('passwordConfirm').addEventListener('keyup', function(e) {
    if (e.key === 'Enter') {
        var password1 = document.getElementById('password').value;
        var password2 = this.value;

        if (password1 === password2) {
            document.getElementById('error-message').style.display = 'none';
            window.location.href = './y_input_page.html';
        } else {
            document.getElementById('error-message').style.display = 'block';
        }
    }
});

