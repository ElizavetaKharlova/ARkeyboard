import cv2 
import numpy as np
import ar_keyboard


#this is the class for the display:
class Display():
    

    def __init__(self):
        # this sets up the video channel 
        self.cap = cv2.VideoCapture(0)
        self.elementArray = []
 
        
    def __del__(self):
        # Destructor to make sure that the capture is released. 
        self.cap.release()

    

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


    def createElement(self, elementType, elementName, elementValue , elementPositon, elementMode)
        # This needs to be run the first time you instantiate a element 
        # Fill the element values and then append it to the elementArray 
        newElement = {
        'Type' : elementType 
        'Name' : elementName
        'Value': elementValue
        'Position' : elementPositon
        'mode' : elementMode
     }
        self.elementArray.append(newElement)
    
    
    def updateElement(self, value, flag , mode):
        # 
        if flag == 'timer':
            #update timer  function 

        elif flag == 'keyboard':
            # display keyboard 

        elif flag == 'target':
            # display target phrase? word??
            # TODO: try 

        elif flag == 'leaderboard':
            # display leaderboard

        elif flag == 'user input':
            # display the user key

        elif flag == 'score':
            # display the score 
        #check the element flag, then do things based on the value of the flag 
        # 1 = keyboard
        # 2 = Target 
        # 3 = Timer


    def readElement(self, elementFlag, elementName):
        #check the element flag, then get the values of the element that is being asked 
        # TODO: How should I store the objects that are on the displa
        
        # the only elements that you will need to read will be keyboard -- its already detecting 
        #  
        return

    
