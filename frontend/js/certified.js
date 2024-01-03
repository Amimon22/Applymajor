// JavaScript

// 파일 업로드 input 태그와 아이콘, 텍스트를 표시할 div 태그를 가져옵니다.
var photoUpload = document.querySelector('.photo-upload');
var addIcon = document.querySelector('.add-icon');
var uploadBox = document.querySelector('.upload-box');

photoUpload.addEventListener('change', function(e) {
    // 사용자가 파일을 선택한 경우
    if(e.target.files.length > 0) {
        // 아이콘을 숨기고
        addIcon.style.display = 'none';

        // 선택한 파일의 이름을 표시합니다.
        var fileNameSpan = document.createElement('span');
        fileNameSpan.style.fontSize = "12px"; // 원하는 폰트 크기
        fileNameSpan.style.width = "200px"; // 원하는 너비
        fileNameSpan.style.fontFamily = "SF Pro"; // 원하는 폰트
        fileNameSpan.textContent = e.target.files[0].name;
        uploadBox.appendChild(fileNameSpan);
    } 
    // 사용자가 파일 선택을 취소한 경우
    else {
        // 아이콘을 다시 표시하고
        addIcon.style.display = 'block';

        // 표시된 파일 이름을 제거합니다.
        if(uploadBox.childNodes.length > 2) {
            uploadBox.removeChild(uploadBox.childNodes[2]);
        }
    }
});

document.getElementById('upload-form').addEventListener('submit', function(event) {
    event.preventDefault();

    var fileInput = document.getElementById('photo-upload');
    var file = fileInput.files[0];
    var formData = new FormData();
    formData.append('photo', file);

    fetch('서버 URL', { // 여기에 실제 서버 URL을 입력해야 합니다.
        method: 'POST',
        body: formData
    })
    .then(function(response) {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        window.location.href = '다음 페이지 URL'; // 여기에 실제 다음 페이지 URL을 입력해야 합니다.
    })
    .catch(function(error) {
        console.error('There has been a problem with your fetch operation:', error);
    });
});
