# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 09:54:37 2020

@author: diada
"""


import cv2
import numpy as np
import time
from matplotlib import pyplot as plt
cap = cv2.VideoCapture('C:/Users/diada/Downloads/blink.avi')
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('C:/Users/diada/Downloads/Copy of 1_blink.avi', fourcc, 80.0, (640,480))
frames=[]


for i in range(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frames.append(gray)
    cv2.imshow('frame', frame)
    time.sleep(.05)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

   # kernel = np.ones((5,5), np.uint8)
def frame_diff(prev_frame, cur_frame, next_frame):
    diff = cv2.absdiff(next_frame, cur_frame)
    return diff

for i in range(1,len(frames)-1):  
    gray=frame_diff(frames[i-1], frames[i], frames[i+1])    
    ret,thresh1 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    gaus = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
    ret,otsu = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    laplacian = cv2.Laplacian(gray, cv2.CV_64F)
    edges = cv2.Canny(gray, 1, 50)
    kernel = np.ones((5,5), np.uint8)
    erosion = cv2.erode(edges, kernel, iterations =1)
    dilation= cv2.dilate(edges, kernel, iterations =1)
    gausblur = cv2.GaussianBlur(gray, (5,5), cv2.BORDER_DEFAULT)
    
    
    _, contours, _= cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    image = cv2.drawContours(edges.copy(), contours, -1, (0,255, 0), 2)
    print(contours) 
    #cv2.imshow('thresh1', thresh1)
    #cv2.imshow('gaus', gaus)
   # cv2.imshow('otsu', otsu)
   # cv2.imshow('laplacian', laplacian)
    #cv2.imshow('gaussian blur', gausblur)
    #cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)
    #cv2.imshow('edges', edges)
    cv2.imshow('gray', gray)
    cv2.imshow('edges.copy()', edges.copy())
    plt.imshow(image)
    
    time.sleep(.25)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break
cv2.waitKey(0)




cap.release()
#out.release()
cv2.destroyAllWindows()

