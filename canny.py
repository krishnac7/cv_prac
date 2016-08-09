import cv2
import numpy as np
from matplotlib import pyplot as plt
def nothing(x):
	pass
min=150
max=200
img=cv2.imread('Lenna.png',0)
edges=cv2.Canny(img,min,max)
cv2.imshow('edge',edges)
cv2.createTrackbar('max','edge',0,255,nothing)
cv2.createTrackbar('min','edge',0,255,nothing)
while True:	
	max=cv2.getTrackbarPos('max','edge')
	min=cv2.getTrackbarPos('min','edge')
	if max<min:
		cv2.setTrackbarPos('max','edge',min+1)
	edges=cv2.Canny(img,min,max)
	cv2.imshow('edge',edges)
	k=cv2.waitKey(1) &0xFF
	if k==27:
		break
cv2.destroyAllWindows()