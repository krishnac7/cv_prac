import numpy as np
import cv2
img=cv2.imread('Lenna.png')
cv2.imshow("original",img)
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(imgray,127,255,0)
_,contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(img,contours,-1,(0,255,0),3)

cnt=contours[4]
cv2.drawContours(img,[cnt],0,(0,255,0),3)
cv2.imshow("contours",img)
cv2.waitKey(0)
