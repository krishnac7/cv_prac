import cv2

img=imread("mad_square.jpg")
ret,thresh=cv2.threshold(img,127,255,0)
_,contours,hierarchy=cv2.findContours(thresh,1,2)\
cnt=contours[0]
epsilon=0.1*cv2.arcLength(cnt,true)
approx=cv2.approxPolyDp(cnt,epsilon,True)
cv2.drawContours