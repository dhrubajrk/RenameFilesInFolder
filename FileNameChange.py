import cv2
import pytesseract
import PIL
import os 
import re
from os import rename
from pytesseract import image_to_string
from PIL import Image

dir_path='C:\\Users\\dhroykar\\Documents\\asp.net kudvenkat\\'
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
for filename in os.listdir(dir_path):
	if "videoplayback" in filename:
		video=cv2.VideoCapture(dir_path+filename)
		success,image=video.read()
		video.release()
		cv2.imwrite('C:\\Users\\dhroykar\\Documents\\demo_img.jpg',image)
		print 'Image captured...'
		frame_text=image_to_string(Image.open('C:\\Users\\dhroykar\\Documents\\demo_img.jpg'))
		print 'OCR done...'
		print frame_text
		
		for line in frame_text.splitlines():
			if "Part" in line:
				newfilename=line+'.mp4'
				break
			else:
				newfilename=filename
		newfilename=re.sub('[/\!?]','',newfilename)
		print 'Renaming to'+newfilename
		os.chdir(dir_path)
		print filename
		os.remove('C:\\Users\\dhroykar\\Documents\\demo_img.jpg')	
		rename(filename,newfilename)
	
	