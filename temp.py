from PIL import Image
from gtts import gTTS
from pdfminer.layout import LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pytesseract import pytesseract
import time
import pygame.mixer


#from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from io import StringIO
from io import open
from urllib.request import urlopen
import docx2txt
#from Fuction.ocr import *
from pdf2image import convert_from_path
import fitz
from pdf2image import convert_from_path, convert_from_bytes

import numpy


pytesseract.tesseract_cmd = r'C:\Anaconda3\envs\Open-Source-Basic-Project\Lib\site-packages\pytesseract\Tesseract-OCR\tesseract.exe'
#pdf to png converter
#pages is number of pages

def pdf2png(filename,pages):
    pdffile = filename
    doc = fitz.open(pdffile)
    for i in range(0,pages):
        page = doc.loadPage(4)  #number of page
        pix = page.getPixmap()

        output = "outfile"+str(i)+".jpg"
        pix.writePNG(output)

#pdf to image converter
def pdf2img_converter(filename):
    pages= convert_from_path(filename,500)

    for pages in pages:
        pages.save('out.jpg','JPEG')

#Image To String 0
def image_to_string(filename):
    img=Image.open(filename)

    #img2=Image.open(filename)
    #img2=deskew(img2)
    #img2=get_grayscale(img2)
    #img2=remove_noise(img2)

    text=pytesseract.image_to_string(img,lang='kor+eng')
    print(text)
    return text


#text to speech function 0
def g_tts(text,file_name,file_type):
    tts=gTTS(text=text,lang='kor')
    save_as=file_name+'.'+file_type
    tts.save(save_as)


#play voice 0
def play_file(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    time.sleep(50)
    pygame.mixer.music.stop()
'''
def pdfparser(data):

    fp = file(data, 'rb')
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process each page contained in the document.

    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
        data =  retstr.getvalue()

    print(data)


'''



def read_pdf_file(pdfFile):
    rsrcmgr=PDFResourceManager()
    retstr=StringIO()
    laparams=LAParams()
    device=TextConverter(rsrcmgr,retstr,laparams=laparams)

    process_pdf(rsrcmgr,device,pdfFile)

    content=retstr.getvalue()
    retstr.close()
    return content

#test1=read_pdf_file('Task8_2017038106.pdf')
#print(test1)

# pdf_file=open("__filename__","rb")
# contents=read_pdf_file(pdf_file)
# contents is text value.

def read_pdf_url(pdfurl):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    process_pdf(rsrcmgr, device, pdfurl)

    content = retstr.getvalue()
    retstr.close()
    return content

#urlopen("urladress")


#docx_to_text 0
def read_docx_file(docxfile):
    text=docx2txt.process(docxfile)

    return text





#pdf2png('../Task8_2017038106.pdf')
#pdf2img_converter('Task8_2017038106.pdf')

#pdf2png('Task8_2017038106.pdf',4)

#pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'


image = image_to_string('2.JPG')
pdf2img_converter('2.JPG')
#a=read_docx_file(r'C:\Users\ygkwo\PycharmProjects\Open210Team_CBNU\Fuction\test1.docx')
#g_tts(a,'test1','mp3')

#print(a)

#play_file('test1.mp3')