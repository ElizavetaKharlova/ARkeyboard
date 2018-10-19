#python stuff
import imutils
import numpy as np
import argparse
import cv2
import matplotlib

class Calibratus_rex(object):

    def __init__(self,image):
    self.image=image
    #this sets the frame that we want to look

    def calib_zone(self):
        cv2.rectangle(self.image,(900,100),(950,150),(255,255,255),3)

    def Get_cal_val(self):
    
        self.cal_val=self.image[925,125]
        print("The Pixel value is:",self.cal)
    
           #     if cv2.waitKey(1) & 0xFF == ord('e'):
          #      break


    def Give_calibration_value(self):
        val = self.cal_val
        return val 


#main function goes here 
cap = cv2.VideoCapture(0)

while True: 
    ret, image = cap.read()
    calibrate = Calibratus_rex(image)

    calibrate.calib_zone()
    calibrate.Get_cal_val()

    skin value = calibrate.Give_calibration_value
    
    cv2.imshow('image',image)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()

