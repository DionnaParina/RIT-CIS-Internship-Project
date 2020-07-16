# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 07:46:03 2020

@author: diada
"""


import cv2
import numpy as np
import time
cap = cv2.VideoCapture('C:/Users/diada/Downloads/blink.avi')
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('C:/Users/diada/Downloads/Copy of 1_blink.avi', fourcc, 80.0, (640,480))
frames=[]
for i in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))):
    ret, frame = cap.read()
    frames.append(frame)
    cv2.imshow('frame', frame)
    time.sleep(1)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break



# Compute the frame difference
def frame_diff(prev_frame, cur_frame, next_frame):
    # Absolute difference between current frame and next frame
    diff_frames1 = cv2.absdiff(next_frame, cur_frame)


cap.release()
#out.release()
cv2.destroyAllWindows()

