import cv2
import numpy as np
img=cv2.imread('Lenna.png')
rows,cols=img.shape[:2]
M=cv2.getRotationMatrix2D((cols/2,rows/2),360,1)
dst=cv2.warpAffine(img,M,(cols,rows))
cv2.imshow("transformed",dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
