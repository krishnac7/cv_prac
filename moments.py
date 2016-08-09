import cv2
import numpy as np
img=cv2.imread('Lenna.png',0)
ret,thresh=cv2.threshold(img,127,255,0)
_,contours,hirerarchy=cv2.findContours(thresh,1,2)
cnt=contours[0]
M=cv2.moments(cnt)
print M
print ""
print cv2.contourArea(contours[0])
print cv2.arcLength(cnt,True)