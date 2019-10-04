# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 19:04:51 2019

@author: kartikay
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

#hsv hue set value
# hue= color
# satutration depth of color
# value(brightness) 0 = black
while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    lower_col=np.array([90,50,20])
    upper_col=np.array([165,255,255])
    
    mask = cv2.inRange(hsv,lower_col,upper_col)
    result = cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("result",result)
    
    k = cv2.waitKey(5) & 0xFF 
    if k == ord('q'):
        break
    
cv2.destroyAllWindows()
cap.release()