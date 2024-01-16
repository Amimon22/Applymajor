document.addEventListener("DOMContentLoaded", function() {
    // 페이지 로딩시 초기 설정
    updateDropdown();

    // MajorBox의 내용이 변경될 때마다 드롭다운 업데이트
    document.getElementById("MajorBox").addEventListener("change", updateDropdown);
  });

  function updateDropdown() {
    var majorBoxContent = document.getElementById("MajorBox").innerText.trim();
    var firstMajor = document.getElementById("firstMajor");
    var secondMajor = document.getElementById("secondMajor");
    var thirdMajor = document.getElementById("thirdMajor");
    var fourthMajor = document.getElementById("fourthMajor");

    // 드롭다운 선택지 초기화
    firstMajor.innerHTML = '<option value=""></option>';
    secondMajor.innerHTML = '<option value=""></option>';
    thirdMajor.innerHTML = '<option value=""></option>';
    fourthMajor.innerHTML = '<option value=""></option>';

    // MajorBox의 내용에 따라 선택지 추가
    if (majorBoxContent === "과학기술대학") {
        addOption(firstMajor, "디지털소프트웨어공학부");
        addOption(firstMajor, "바이오공학전공");
        addOption(firstMajor, "생활체육학전공");
        addOption(firstMajor, "식품영양학전공");
        addOption(firstMajor, "정보통계학전공");
        addOption(firstMajor, "화학전공");
        addOption(firstMajor, "수학전공");

    } else if (majorBoxContent === "글로벌융합대학") {
        addOption(selectMajor, "국어국문학전공");
        addOption(selectMajor, "일어일문학전공");
        addOption(selectMajor, "중어중문학전공");
        addOption(selectMajor, "영어영문학전공");
        addOption(selectMajor, "불어불문학전공");
        addOption(selectMajor, "독어독문학전공");
        addOption(selectMajor, "스페인어전공");
        addOption(selectMajor, "사학전공");
        addOption(selectMajor, "철학전공");
        addOption(selectMajor, "미술사학전공");
        addOption(selectMajor, "문화인류학전공");
        addOption(selectMajor, "경영학전공");
        addOption(selectMajor, "회계학전공");
        addOption(selectMajor, "국제통상학전공");                        
        addOption(selectMajor, "법학전공");
        addOption(selectMajor, "사회학전공");
        addOption(selectMajor, "문헌정보학전공");
        addOption(selectMajor, "심리학전공");
        addOption(selectMajor, "아동가족학전공");
        addOption(selectMajor, "사회복지학전공");
        addOption(selectMajor, "정치외교학전공");
        addOption(selectMajor, "의상디자인전공");

    } else if (majorBoxContent === "아트앤디자인") {
        addOption(selectMajor, "동양화전공");
        addOption(selectMajor, "서양화전공");
        addOption(selectMajor, "실내디자인전공");
        addOption(selectMajor, "시각디자인전공");
        addOption(selectMajor, "텍스타일디자인전공");
        
    }
        // 필요에 따라 다른 대학 또는 전공들을 추가
  }

  function addOption(selectElement, optionText) {
      var option = document.createElement("option");
      option.value = optionText;
      option.text = optionText;
      selectElement.add(option);
  }