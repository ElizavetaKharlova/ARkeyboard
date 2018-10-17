import cv2 
import numpy as np

#this is the class for the display:
class Display():

    def __init__(self):
        # this sets up the video channel 
        self.cap = cv2.VideoCapture(0)
        return None
    def __del__(self):
        # Destructor to make sure that the capture is released. 
        self.cap.release()
        return None
    def readframe(self):
        self.ret, self.image = cap.read()
        return 
    def updateElement(self, elementFlag, elementValues):
        #check the element flag, then do things based on the value of the flag 


        return
    def readElement(self, elementFlag):
        #check the element flag, then get the values of the element that is being asked 
        
        
        return

    #img = image.copy()
    #img = cv2.flip(img,1)
    #gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #ret1, thresh = cv2.threshold(gray, 115, 255, cv2.THRESH_BINARY)
    #kernel = np.ones((3,3),np.uint8)
    #opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN, kernel, iterations = 3)
    #font = cv2.FONT_HERSHEY_COMPLEX
    