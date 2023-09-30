import cv2 as cv
import numpy as np
import serial as s
serial = s.Serial('COM5',9600)

cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
   # green = np.uint8([[[0,255,0]]])
    #hsv_green = cv.cvtColor(green,cv.COLOR_BGR2HSV)
    #print(hsv_green)
    # green = 60,255,255
    lower_green = np.array([36,100,100])
    upper_green = np.array([89,255,255])
    lowerred = np.array([120,50,70])
    upperred = np.array([180,255,255])
    lowerblue = np.array([90,50,70])
    upperblue = np.array([128,255,255])
    

#mask
    mask_green = cv.inRange(hsv,lower_green,upper_green)
    mask_blue = cv.inRange(hsv,lowerblue, upperblue) 
    mask_red = cv.inRange(hsv,lowerred, upperred)
    mask_total = mask_green + mask_blue + mask_red
    if np.sum(mask_red) > np.sum(mask_green) and np.sum(mask_red) > np.sum(mask_blue):
        serial.write(b'r')
        print("Red detected")
    if np.sum(mask_green) > np.sum(mask_red) and np.sum(mask_green) > np.sum(mask_blue):
        serial.write(b'g')
        print("Green detected")
    if np.sum(mask_blue) > np.sum(mask_green) and np.sum(mask_blue) > np.sum(mask_red):
        serial.write(b'b')
        print("Blue detected")
    result = cv.bitwise_and(frame,frame,mask = mask_total)
    cv.imshow('result',result)
    key = cv.waitKey(5)
    if key == 27:
        break
    # chaneg the color to hsv format: hue, saturation. value
