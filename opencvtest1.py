# -*- coding: utf-8 -*-
import numpy as np
import cv2

#cap = cv2.VideoCapture('movie2.mov')
#cap = cv2.VideoCapture('movie3.m4v')
cap = cv2.VideoCapture('videoplayback.mp4')
ret, frame = cap.read()
frame1 = frame
frame2 = frame
accumulate = cv2.subtract(frame,frame)

while(cap.isOpened()):
	ret, frame = cap.read()
	frame1 = frame
	#difference = cv2.subtract(frame2,frame1)
	frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
	frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
	difference = cv2.subtract(frame2,frame1)
	#difference = cv2.equalizeHist(difference)
	#thresh,difference = cv2.threshold(difference,20,255,cv2.THRESH_TOZERO)
	difference = cv2.equalizeHist(difference)
	#difference= cv2.adaptiveThreshold(difference,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,3)
	#difference = cv2.adaptiveThreshold(difference,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_TOZERO,21,3)
	#difference = cv2.threshold(difference,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
	#difference = cv2.bitwise_not(difference);
	#accumulate += difference
	#difference = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	difference = cv2.applyColorMap(difference, cv2.COLORMAP_JET)
	frame2 = frame
	cv2.imshow('frame',difference)
	#cv2.imshow('frame',accumulate)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()