import cv2
import numpy as np
cap=cv2.VideoCapture(0)
while(1):
        _,frame=cap.read()
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        cv2.imshow("hsv image",hsv)
        lower_blue=np.array([110,50,50])
        upper_blue=np.array([130,255,255])
        lower_green=np.array([50,100,100])
        upper_green=np.array([70,255,255])
        lower_red=np.array([0,100,100])
        upper_red=np.array([10,255,255])
        
        mask_blue=cv2.inRange(hsv,lower_blue,upper_blue)
        mask_green=cv2.inRange(hsv,lower_green,upper_green)
        mask_red=cv2.inRange(hsv,lower_red,upper_red)

        red_frame=cv2.bitwise_and(frame,frame,mask=mask_red)
        blue_frame=cv2.bitwise_and(frame,frame,mask=mask_blue)
        green_frame=cv2.bitwise_and(frame,frame,mask=mask_green)

        cv2.imshow("feed",frame)
        cv2.imshow("red",red_frame)
        cv2.imshow("green",green_frame)
        cv2.imshow("blue",blue_frame)
        k=cv2.waitKey(1) & 0xFF
        if k==113:
            break
cv2.destroyAllWindows()
