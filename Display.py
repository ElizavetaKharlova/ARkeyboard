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
        # This function gets the frames from the capture feed 
        ret, image = cap.read()
        img = image.copy()
        img = cv2.flip(img,1)
        det = img.copy()

        self.frames ={
            'detection' : det,
            'image' : img,
        }
               
         return self.frames


    def createElement(self, **element)
        # This needs to be run the first time you instantiate a element 


    def updateElement(self, **element):
        # 
        
        #check the element flag, then do things based on the value of the flag 
        # 1 = keyboard
        # 2 = Target 
        # 3 = Timer
        
        eleType = element.get('Element Type')
        
        return
    def readElement(self, elementFlag, elementName):
        #check the element flag, then get the values of the element that is being asked 
        # TODO: How should I store the objects that are on the displa
        
        return

    element = {
        'Element Type' : 
        'Element Name' :
        'Element Value':

    }

    #img = image.copy()
    #img = cv2.flip(img,1)
    #gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #ret1, thresh = cv2.threshold(gray, 115, 255, cv2.THRESH_BINARY)
    #kernel = np.ones((3,3),np.uint8)
    #opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN, kernel, iterations = 3)
    #font = cv2.FONT_HERSHEY_COMPLEX
    