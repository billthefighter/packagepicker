# -*- coding: utf-8 -*-
#This file exists to test the process shown here: http://docs.opencv.org/trunk/d7/d8b/tutorial_py_face_detection.html
#This file also exists to show how computer vision detects tom cruise

import numpy as np
import cv2

   
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

poop = cv2.imread('tomcruise.jpg')
poop2 = cv2.imread('tomcruise2.jpg')
poop3 = cv2.imread('tomcruise3.jpg')
poop4 = cv2.imread('lwphoto.jpg')
poop5 = cv2.imread('lwphoto2.jpg')
poop6 = cv2.adaptiveThreshold(cv2.cvtColor(poop2, cv2.COLOR_BGR2GRAY),255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,3,3)
print poop6.shape
print len(poop6.shape)
print len(poop.shape)
def facedetect(img):
	#check if image is already grayscale
	if len(img.shape) > 2: 
		gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	else:
		gray = img

	faces = face_cascade.detectMultiScale(gray, 1.3, 5)
	for (x,y,w,h) in faces:
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
		roi_gray = gray[y:y+h, x:x+w]
		roi_color = img[y:y+h, x:x+w]
		eyes = eye_cascade.detectMultiScale(roi_gray)
		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
	return(img)


cv2.imshow('farts',facedetect(poop))
cv2.imshow('farts2',facedetect(poop2))
cv2.imshow('farts3',facedetect(poop3))
cv2.imshow('farts4',facedetect(poop4))
cv2.imshow('farts5',facedetect(poop5))
cv2.imshow('farts6',facedetect(poop6))
cv2.waitKey(0)
cv2.destroyAllWindows()