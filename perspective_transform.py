import cv2
import numpy as np
import matplotlib.pyplot as plt
img=cv2.imread('sudoko02.jpeg')
rows,cols,ch=img.shape
pts1=np.float32([[50,223],[389,208],[31,578],[416,580]])
pts2=np.float32([[0,0],[300,0],[0,300],[300,300]])
M=cv2.getPerspectiveTransform(pts1,pts2)
dst=cv2.warpPerspective(img,M,(300,300))

plt.subplot(121),plt.imshow(img),plt.title("Input")
plt.subplot(122),plt.imshow(dst),plt.title("outpt")
plt.show()
