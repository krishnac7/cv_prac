import cv2
import numpy as np 
img =cv2.imread('j.png',0)
img2=cv2.imread('opening.png')
img3=cv2.imread('closing.png')
cv2.imshow("original",img)

kernel=np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations=1)
dilation=cv2.dilate(img,kernel,iterations=1)
opening=cv2.morphologyEx(img2,cv2.MORPH_OPEN,kernel)
closing=cv2.morphologyEx(img3,cv2.MORPH_CLOSE,kernel)
gradient=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kernel)
tophat=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kernel)
blackhat=cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kernel)

cv2.imshow("eroded",erosion)
cv2.imshow("dilated",dilation)
cv2.imshow("opening ",opening)
cv2.imshow("closing",closing)
cv2.imshow("Gradient",gradient)
cv2.imshow("Top hat",tophat)
cv2.imshow("black hat",cv2.MORPH_BLACKHAT,kernel)
cv2.waitKey(0)