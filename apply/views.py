from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from PIL import Image
import pytesseract
import os
from .models import Academic
from .models import Apply
from .models import Departure_Major_Code
from django.http import HttpResponse
from .forms import MajorForm


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def ocr_read(request):
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
            
    context['imgname'] = imgname
    context['resulttext'] = resulttext.replace(" ","")
        
    return render(request, 'ocr.html', context)


# def apply_link(request):   #학부에 맞는 지망선택 창으로 연결  
#     if (Academic.major == '글로벌융합대학'):
#         return render(request, 'global_major_choose.html')
#     elif (Academic.major == '과학기술대학'):
#         return render(request, 'science_major_choose,html')
#     elif (Academic.major == 'Art&Design대학'):
#         return render(request, 'art_major_choose.html')


def apply_create(request):
    if request.method == "POST":
        form = MajorForm(request.POST, user=request.user)
        if form.is_valid():
            academic = form.save(commit=False)
            academic.user = request.user
            academic.save()
            return redirect('home')
    else:
        form = MajorForm(user=request.user)
    return render(request, 'apply_create.html', {'form': form})