function checkOnlyOne(element) {
  const checkboxes = document.getElementsByName("department");
  checkboxes.forEach((cb) => {
    cb.checked = false;
  });
  element.checked = true;
}

var checkboxes = document.getElementsByName("department");
var global_check = document.getElementById("global");
var science_check = document.getElementById("science");
var art_check = document.getElementById("art");

var dropdownGlobal = document.createElement("select");
var dropdownScience = document.createElement("select");
var dropdownArt = document.createElement("select");

var dropdownGlobal2 = document.createElement("select");
var dropdownScience2 = document.createElement("select");
var dropdownArt2 = document.createElement("select");

var dropdownGlobal3 = document.createElement("select");
var dropdownScience3 = document.createElement("select");
var dropdownArt3 = document.createElement("select");

var dropdownGlobal4 = document.createElement("select");
var dropdownScience4 = document.createElement("select");
var dropdownArt4 = document.createElement("select");

var firstChoice = document.querySelector('.h3');
var secondChoice = document.querySelector('.h4');
var thirdChoice = document.querySelector('.h5');
var fourthChoice = document.querySelector('.h6');


var globalOptions = [
  "국어국문학전공",
  "일어일문학전공",
  "중어중문학전공",
  "영어영문학전공",
  "불어불문학전공",
  "독어독문학전공",
  "스페인어전공",
  "사학전공",
  "철학전공",
  "미술사학전공",
  "문화인류학전공",
  "경영학전공",
  "회계학전공",
  "국제통상학전공",
  "법학전공",
  "사회학전공",
  "문헌정보학전공",
  "심리학전공",
  "아동가족학전공",
  "사회복지학전공",
  "정치외교학전공",
  "의상디자인전공"
];
var scienceOptions = ["디지털소프트웨어공학부",
"바이오공학전공",
"생활체육학전공",
"식품영양학전공",
"정보통계학전공",
"화학전공",
"수학전공"
];
var artOptions =  ["동양화전공",
"서양화전공",
"실내디자인전공",
"시각디자인전공",
"텍스타일디자인전공"];
// 체크박스의 상태 변화 감지

globalOptions.forEach((option) => {
  var optionElement = document.createElement("option");
  optionElement.text = option;
  dropdownGlobal.add(optionElement);

  var optionElement2 = document.createElement("option");
  optionElement2.text = option;
  dropdownGlobal2.add(optionElement2);

  var optionElement3 = document.createElement("option");
  optionElement3.text = option;
  dropdownGlobal3.add(optionElement3);

  var optionElement4 = document.createElement("option");
  optionElement4.text = option;
  dropdownGlobal4.add(optionElement4);
});

scienceOptions.forEach((option) => {
  var optionElement = document.createElement("option");
  optionElement.text = option;
  dropdownScience.add(optionElement);

  var optionElement2 = document.createElement("option");
  optionElement2.text = option;
  dropdownScience2.add(optionElement2);

  var optionElement3 = document.createElement("option");
  optionElement3.text = option;
  dropdownScience3.add(optionElement3);

  var optionElement4 = document.createElement("option");
  optionElement4.text = option;
  dropdownScience4.add(optionElement4);
});

artOptions.forEach((option) => {
  var optionElement = document.createElement("option");
  optionElement.text = option;
  dropdownArt.add(optionElement);

  var optionElement2 = document.createElement("option");
  optionElement2.text = option;
  dropdownArt2.add(optionElement2);

  var optionElement3 = document.createElement("option");
  optionElement3.text = option;
  dropdownArt3.add(optionElement3);

  var optionElement4 = document.createElement("option");
  optionElement4.text = option;
  dropdownArt4.add(optionElement4);
}); // 좌표와 크기 설정

// 드롭다운 리스트 초기 상태는 숨김으로 설정
dropdownGlobal.style.display = "none";
dropdownGlobal2.style.display = "none"; 
dropdownGlobal3.style.display = "none"; 
dropdownGlobal4.style.display = "none";

dropdownScience.style.display = "none";
dropdownScience2.style.display = "none"; 
dropdownScience3.style.display = "none"; 
dropdownScience4.style.display = "none";

dropdownArt.style.display = "none";
dropdownArt2.style.display = "none"; 
dropdownArt3.style.display = "none"; 
dropdownArt4.style.display = "none";


var rectangle = document.querySelector('.rounded-rectangle');
rectangle.style.display = "none";

var globaltext = document.querySelector('.global-text');
var sciencetext = document.querySelector('.science-text');
var arttext = document.querySelector('.art-text');

var rect1 = document.querySelector('.rect1');
var rect2 = document.querySelector('.rect2');
var rect3 = document.querySelector('.rect3');
var rect4 = document.querySelector('.rect4');

var text1 = document.querySelector('.text1');
var text2 = document.querySelector('.text2');
var text3 = document.querySelector('.text3');
var text4 = document.querySelector('.text4');


globaltext.style.display = "none";
sciencetext.style.display = "none";
arttext.style.display = "none";

rect1.style.display = "none";
rect2.style.display = "none";
rect3.style.display = "none";
rect4.style.display = "none";

text1.style.display = "none";
text2.style.display = "none";
text3.style.display = "none";
text4.style.display = "none";

checkboxes.forEach((checkbox) => {
  checkbox.addEventListener("change", function () {
    // 체크박스가 체크되었는지 확인
    if (global_check.checked) {
      rectangle.style.display = "block";
      globaltext.style.display = "block";
      text1.style.display = "block";
      text2.style.display = "block";
      text3.style.display = "block";
      text4.style.display = "block";   
      rect1.style.display = "block";
      rect2.style.display = "block";
      rect3.style.display = "block";
      rect4.style.display = "block";

      dropdownGlobal.style.display="block";
      dropdownGlobal.style.position = "absolute";
      dropdownGlobal.style.top = "400px";
      dropdownGlobal.style.left ="190px";
      dropdownGlobal.style.fontFamily = "SF Pro Text";
      dropdownGlobal.style.fontSize = "14px";
      dropdownGlobal.style.color = "#2c2c2c";
      dropdownGlobal.style.fontWeight = "600";

      dropdownGlobal2.style.display="block";
      dropdownGlobal2.style.position = "absolute";
      dropdownGlobal2.style.top = "490px";
      dropdownGlobal2.style.left = "190px";
      dropdownGlobal2.style.fontFamily = "SF Pro Text";
      dropdownGlobal2.style.fontSize = "14px";
      dropdownGlobal2.style.color = "#2c2c2c";
      dropdownGlobal2.style.fontWeight = "600";   

      dropdownGlobal3.style.display="block";
      dropdownGlobal3.style.position = "absolute";
      dropdownGlobal3.style.top = "580px";
      dropdownGlobal3.style.left = "190px";
      dropdownGlobal3.style.fontFamily = "SF Pro Text";
      dropdownGlobal3.style.fontSize = "14px";
      dropdownGlobal3.style.color = "#2c2c2c";
      dropdownGlobal3.style.fontWeight = "600";   

      dropdownGlobal4.style.display="block";
      dropdownGlobal4.style.position = "absolute";
      dropdownGlobal4.style.top = "670px";
      dropdownGlobal4.style.left = "190px";
      dropdownGlobal4.style.fontFamily = "SF Pro Text";
      dropdownGlobal4.style.fontSize = "14px";
      dropdownGlobal4.style.color = "#2c2c2c";
      dropdownGlobal4.style.fontWeight = "600";   

    } else {
      globaltext.style.display = "none";
      dropdownGlobal.style.display = "none";
      dropdownGlobal2.style.display = "none"; 
      dropdownGlobal3.style.display = "none"; 
      dropdownGlobal4.style.display = "none";  // 체크가 해제되면 드롭다운 리스트를 숨깁니다.
    }
    if (science_check.checked) {
      rectangle.style.display = "block";
      sciencetext.style.display = "block";
      text1.style.display = "block";
      text2.style.display = "block";
      text3.style.display = "block";
      text4.style.display = "block";   
      rect1.style.display = "block";
      rect2.style.display = "block";
      rect3.style.display = "block";
      rect4.style.display = "block";

      dropdownScience.style.display="block";
      dropdownScience.style.position = "absolute";
      dropdownScience.style.top = "400px";
      dropdownScience.style.left ="190px";
      dropdownScience.style.fontFamily = "SF Pro Text";
      dropdownScience.style.fontSize = "14px";
      dropdownScience.style.color = "#2c2c2c";
      dropdownScience.style.fontWeight = "600";     

      dropdownScience2.style.display="block";
      dropdownScience2.style.position = "absolute";
      dropdownScience2.style.top = "490px";
      dropdownScience2.style.left = "190px";
      dropdownScience2.style.fontFamily = "SF Pro Text";
      dropdownScience2.style.fontSize = "14px";
      dropdownScience2.style.color = "#2c2c2c";
      dropdownScience2.style.fontWeight = "600";     

      dropdownScience3.style.display="block";
      dropdownScience3.style.position = "absolute";
      dropdownScience3.style.top = "580px";
      dropdownScience3.style.left = "190px";
      dropdownScience3.style.fontFamily = "SF Pro Text";
      dropdownScience3.style.fontSize = "14px";
      dropdownScience3.style.color = "#2c2c2c";
      dropdownScience3.style.fontWeight = "600";     

      dropdownScience4.style.display="block";
      dropdownScience4.style.position = "absolute";
      dropdownScience4.style.top = "670px";
      dropdownScience4.style.left = "190px";
      dropdownScience4.style.fontFamily = "SF Pro Text";
      dropdownScience4.style.fontSize = "14px";
      dropdownScience4.style.color = "#2c2c2c";
      dropdownScience4.style.fontWeight = "600";     

    } else {
      sciencetext.style.display = "none";
      dropdownScience.style.display = "none";
      dropdownScience2.style.display = "none";
      dropdownScience3.style.display = "none";
      dropdownScience4.style.display = "none"; // 체크가 해제되면 드롭다운 리스트를 숨깁니다.
    }
    if (art_check.checked) {
      rectangle.style.display = "block";
      arttext.style.display = "block";
      text1.style.display = "block";
      text2.style.display = "block";
      text3.style.display = "block";
      text4.style.display = "block";   
      rect1.style.display = "block";
      rect2.style.display = "block";
      rect3.style.display = "block";
      rect4.style.display = "block";

      dropdownArt.style.display="block";
      dropdownArt.style.position = "absolute";
      dropdownArt.style.top = "400px";
      dropdownArt.style.left ="190px";
      dropdownArt.style.fontFamily = "SF Pro Text";
      dropdownArt.style.fontSize = "14px";
      dropdownArt.style.color = "#2c2c2c";
      dropdownArt.style.fontWeight = "600";     

      dropdownArt2.style.display="block";
      dropdownArt2.style.position = "absolute";
      dropdownArt2.style.top = "490px";
      dropdownArt2.style.left = "190px";
      dropdownArt2.style.fontFamily = "SF Pro Text";
      dropdownArt2.style.fontSize = "14px";
      dropdownArt2.style.color = "#2c2c2c";
      dropdownArt2.style.fontWeight = "600";   

      dropdownArt3.style.display="block";
      dropdownArt3.style.position = "absolute";
      dropdownArt3.style.top = "580px";
      dropdownArt3.style.left = "190px";
      dropdownArt3.style.fontFamily = "SF Pro Text";
      dropdownArt3.style.fontSize = "14px";
      dropdownArt3.style.color = "#2c2c2c";
      dropdownArt3.style.fontWeight = "600";   

      dropdownArt4.style.display="block";
      dropdownArt4.style.position = "absolute";
      dropdownArt4.style.top = "670px";
      dropdownArt4.style.left = "190px";
      dropdownArt4.style.fontFamily = "SF Pro Text";
      dropdownArt4.style.fontSize = "14px";
      dropdownArt4.style.color = "#2c2c2c";
      dropdownArt4.style.fontWeight = "600";   
    } else {
      arttext.style.display = "none";
      dropdownArt.style.display = "none";
      dropdownArt2.style.display = "none";
      dropdownArt3.style.display = "none";
      dropdownArt4.style.display = "none"; // 체크가 해제되면 드롭다운 리스트를 숨깁니다.
    }
  });
});

document.body.appendChild(dropdownGlobal);
document.body.appendChild(dropdownScience);
document.body.appendChild(dropdownArt);
document.body.appendChild(dropdownGlobal2);
document.body.appendChild(dropdownScience2);
document.body.appendChild(dropdownArt2);
document.body.appendChild(dropdownGlobal3);
document.body.appendChild(dropdownScience3);
document.body.appendChild(dropdownArt3);
document.body.appendChild(dropdownGlobal4);
document.body.appendChild(dropdownScience4);
document.body.appendChild(dropdownArt4);



var burger = $('.menu-trigger');

burger.each(function(index){
  var $this = $(this);
  
  $this.on('click', function(e){
    e.preventDefault();
    $(this).toggleClass('active-' + (index+1));
  })
});