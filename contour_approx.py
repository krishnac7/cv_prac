import cv2

img=cv2.imread("Lenna.png",0)
ret,thresh=cv2.threshold(img,127,255,0)
_,contour,hierarchy=cv2.findContours(img.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnt=contour[0]
epsilon=0.1*cv2.arcLength(cnt,True)
approx=cv2.approxPolyDP(cnt,epsilon,True)
cv2.drawContours(img, approx, -1, (0,255,130), 3)
cv2.imshow("approx",img)
cv2.waitKey(0)