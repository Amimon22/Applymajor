from django.shortcuts import render
from django.views import View
from django.core.files.storage import FileSystemStorage
from PIL import Image
import pytesseract
import os, re
from django.utils import timezone
from .models import Source, Academic, Course, Major, Grade, Choice, User_apply_profile
from django.http import HttpRequest

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_read(request: HttpRequest, category: int):
    context={}
    
    imgname = ''
    resulttext = ''
    
    if 'uploadfile' in request.FILES:
        uploadfile = request.FILES.get('uploadfile', '')
        
        if uploadfile != '':
            name_old = uploadfile.name
            name_ext = os.path.splitext(name_old)[1]

            fs = FileSystemStorage(location='static/source')
            imgname = fs.save(f"src-{name_old}", uploadfile)
            
            imgfile = Image.open(f"./static/source/{imgname}")
            resulttext = pytesseract.image_to_string(imgfile, lang='kor+eng')
            
            user_instance = request.user

            source_instance = Source(
                user=user_instance,
                src_file=imgname,
                src_name=name_old,
                src_link=(f"src-{name_old}", uploadfile),
                result_text=resulttext.replace(" ", ""),
                status=True,
                usage_flag='',
                create_at=timezone.now()
            )
            
            source_instance.save()
            
            if category == 1:
                # 학적 정보 추출
                student_number = extract_student_id(resulttext)
                academic_status = extract_academic_status(resulttext)
                grade = extract_grade(resulttext)
                major = extract_major(resulttext)

                # 학적 정보 저장
                academic_instance = Academic(
                    user=user_instance,
                    student_number=student_number,
                    academic_status=academic_status,
                    grade=grade,
                    major=major
                )

                academic_instance.save()
            
            elif category == 2:
                # 수강 정보 추출
                course_code = extract_course_code(request, resulttext)
                course_name = extract_course_name(course_code)

                # 수강 정보 저장
                course_instance = Course(
                    user=user_instance,
                    course_code=course_code,
                    course_name=course_name
                )
                
                course_instance.save()

            elif category == 3:
                # 성적 정보 추출
                grades = extract_grades(resulttext)
                course_credits = extract_course_credits(resulttext)

                # 성적 정보 저장
                for grade_info in grades:
                    grade_instance = Grade(
                        user=user_instance,
                        grades1=grades[0],
                        grades2=grades[1],
                        course_credits1=course_credits[0],
                        course_credits2=course_credits[1]
                    )
                    grade_instance.save()
            
    context['imgname'] = imgname
    context['resulttext'] = resulttext.replace(" ","")
        
    return render(request, 'ocr.html', context)

def extract_student_id(resulttext):
    match = re.search(r'\d{8,}', resulttext)
    
    if match:
        student_id = match.group()[:8]
        return student_id
    else:
        return ''

def extract_academic_status(resulttext):
    if '재학' in resulttext:
        return '재학'
    elif '휴학' in resulttext:
        return '휴학'
    else:
        return ''

def extract_grade(resulttext):
    match = re.search(r'\d+\(\d+\)', resulttext)
    
    if match:
        return match.group()
    else:
        return ''
    
def extract_major(resulttext):
    department_patterns = ['과학기술대학', '글로벌융합대학', 'Art&Design대학']

    for pattern in department_patterns:
        if pattern in resulttext:
            return pattern
    
    return ''

def extract_course_code(request: HttpRequest, resulttext):
    course_codes = re.findall(r'\d{6}', resulttext)
    
    codes = ['502241', '502242', '502243', '502388', '502387', '502245', '502246', '502247', '502248', '502249', '502407', '502251', '502252', '502253', '502254', '502255', '502257', '502256', '502258', '502259', '502260', '502831', '502263', '502264', '502265', '502266', '502267', '502268', '502269', '502270', '502271', '502272', '502273', '502274', '502289', '502290', '502878', '502927', '502854', '502275', '502276', '502277', '502278', '502279', '502280', '502832', '502281', '502291', '502292', '502293', '502294', '502295', '502296', '502297', '502298', '502299', '502300']
    
    matching_codes = [code for code in course_codes if code in codes]
    
    return matching_codes

def extract_course_name(course_code):
    related_majors = {}

    for code in course_code:
        # Subject_code 모델에서 해당 code에 매칭되는 Major를 가져옴
        majors = Major.objects.filter(subject_codes__code=code)

        if majors.exists():
            # 만약 일치하는 Major가 있다면, related_majors에 저장
            related_majors[code] = majors

    return related_majors


def extract_grades(resulttext):
    grades = [None, None]  # Initialize grades list

    # Extracting grades for 1st semester
    index_1st_semester = resulttext.find('1학기') + 3
    if index_1st_semester > 2:
        grades[0] = resulttext[index_1st_semester : index_1st_semester + 6]

    # Extracting grades for 2nd semester
    index_2nd_semester = resulttext.find('2학기') + 3
    if index_2nd_semester > 2:
        grades[1] = resulttext[index_2nd_semester : index_2nd_semester + 6]

    print(grades)
    return grades

def extract_course_credits(resulttext):
    course_credits = [None, None]  # Initialize course_credits list

    # Extracting course credits for 1st semester
    index_1st_semester = resulttext.find('1학기') + 3
    if index_1st_semester > 2:
        course_credits[0] = int(resulttext[index_1st_semester + 2 : index_1st_semester + 4])

    # Extracting course credits for 2nd semester
    index_2nd_semester = resulttext.find('2학기') + 3
    if index_2nd_semester > 2:
        course_credits[1] = int(resulttext[index_2nd_semester + 2 : index_2nd_semester + 4])

    print(course_credits)
    return course_credits


def validate_and_get_integer(value, min_value, max_value):
    try:
        validated_value = int(value)
        return min(max(validated_value, min_value), max_value)
    except ValueError:
        return None

def validate_and_get_decimal(value, min_value, max_value):
    try:
        validated_value = float(value)
        return min(max(validated_value, min_value), max_value)
    except ValueError:
        return None
    
class Apply_result(View):
    def get(self, request):
        users = User_apply_profile.objects.all()
        majors = Major.objects.all()
        
        competition_data = []
        
        for major in majors:
            model_data = {'major': major, 'user_data': []}

            for user_profile in users:
                rank = user_profile.get_1st_priority_rank(major)
                competition_rate = user_profile.calculate_competition_rate(major)
                username = user_profile.get_username()

                user_data = {
                    'user': user_profile.user,
                    'rank': rank,
                    'competition_rate': competition_rate,
                }

                model_data['user_data'].append(user_data)

            competition_data.append(model_data)

        return render(request, 'apply_result.html', {'competition_data': competition_data})