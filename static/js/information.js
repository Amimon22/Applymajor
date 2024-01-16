document.querySelector('.purple-shape .consent').addEventListener('click', function() {
    const grayShape = document.querySelector('.gray-shape');
    grayShape.style.animation = 'slide-down 1s forwards';
});

document.querySelector('.check input').addEventListener('change', function(e) {
    if (e.target.checked) {
        document.querySelector('.next-btn').style.display = 'block';
    } else {
        document.querySelector('.next-btn').style.display = 'none';
    }
});

document.querySelector('.next-btn').addEventListener('click', function() {
    window.location.href = 'chating_page_ver1.html';
});
