from PIL import Image,ImageDraw,ImageFont
import qrcode
from src import get
from src import generate

def content(img,content): #kurs adı
    name = content
    font = ImageFont.truetype("arial.ttf", size = 100)
    d = ImageDraw.Draw(img)
    y_pix = 1150
    stp = 850
    d.text((get.start_pix_di(name,font,stp),y_pix),name, fill=(0,0,0),font = font)
def qr(img):
    qr = generate.qr()
    qr = qr.resize((250,250), Image.ANTIALIAS)
    offset = (2922,2040)
    img.paste(qr,offset)

def instructor(img):
    text = get.instructor()
    stp = 2630
    font = ImageFont.truetype("arial.ttf", size=65)
    d = ImageDraw.Draw(img)
    y_pix = 1930
    d.text((get.start_pix_di(text, font, stp), y_pix), text, fill=(0, 0, 0), font=font)

def date(img,date):
    text = date
    stp = 1500
    font = ImageFont.truetype("arial.ttf", size=65)
    d = ImageDraw.Draw(img)
    y_pix = 2230
    d.text((get.start_pix_di(text, font, stp), y_pix), text, fill=(0, 0, 0), font=font)

def name(img,user):
    name = user
    font = ImageFont.truetype("arial.ttf", size = 200)
    d = ImageDraw.Draw(img)
    stp = 2120
    y_pix = 882
    d.text((get.start_pix_di(name,font,stp),y_pix),name, fill=(0,0,0,255),font = font)