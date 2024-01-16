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


// document.getElementById('studentID').addEventListener('keydown', function(e) {
//     if (e.key === 'Enter' && this.value) {  // 엔터 키를 눌렀고, 입력 필드에 텍스트가 있을 때
//         // 서버에 데이터를 전송하는 코드를 이곳에 추가해주세요.


//         setTimeout(function() {
//             document.querySelector('.memon_chat2').classList.add('fade-in');
//         }, 500);  // .memon_chat2를 0.5초 후에 보이게 함

//         setTimeout(function() {
//             document.querySelector('.user_chat2').classList.add('fade-in');
//         }, 1000);  // .user_chat2를 1초 후에 보이게 함
//    }
// }); 

document.getElementById('password').addEventListener('keydown', function(e) {
    if (e.key === 'Enter') {  // 엔터 키를 눌렀을 때
        var password1 = document.querySelector('.user_chat2').value;
        var password2 = this.value;

        if (password1 === password2) {
            // 비밀번호가 일치하면 웹페이지를 넘어갑니다.
            window.location.href = 'nextpage.html';  // 이 URL은 실제 다음 페이지의 URL로 변경해야 합니다.
        } else {
            // 비밀번호가 일치하지 않으면 오류 메시지를 표시합니다.
            document.getElementById('error-message').style.display = 'block';
        }

        setTimeout(function() {
            document.querySelector('.memon_chat3').classList.add('fade-in');
        }, 500);  // .memon_chat3를 0.5초 후에 보이게 함

        setTimeout(function() {
            document.querySelector('.user_chat3').classList.add('fade-in');
        }, 1000);  // .user_chat3를 1초 후에 보이게 함
    }
});