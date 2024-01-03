from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from PIL import Image
import pytesseract
import os

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