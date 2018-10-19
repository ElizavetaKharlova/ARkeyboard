import cv2 
import numpy as np
import ar_keyboard


#this is the class for the display:
class Display():
    def __init__(self):
        # this sets up the video channel 
        self.cap = cv2.VideoCapture(0)
        self.frames = {}
        self.elements = {}
        
    def __del__(self):
        # Destructor to make sure that the capture is released. 
        self.cap.release()

    def read_camera(self):
        # This function gets the frames from the capture feed 
        ret, image = self.cap.read()
        img = cv2.flip(image.copy(), 1)

        self.frames ={
            'camera' : img,
            'detection' : img.copy(),
            'display': img.copy()
        }
        # return self.frames

    def create_element(self, element_type, element_value, element_positon, element_mode):
        # This needs to be run the first time you instantiate a element 
        # Fill the element values and then append it to the elementArray
        # for the record the above design is stupid. Change element array to a dict.
        self.elements[element_type] = {
            #'Name' : element_name,
            'value': element_value,
            'position' : element_positon,
            'mode' : element_mode
        }

        #WHAT THE FUCK IS THIS???
        # cv2.rectangle(self.frames('image'),(xTL, yTL), (xBR,yBR), (255,255,255),3) 
        # self.element_array.append(newElement)
    

    def element_exists(self, element_type):
        return element_type in self.elements

        # for i in range(0, len(self.elementArray)):
        #     if self.elementArray[i].get('Type') == flag:
        #         #this means that there is already a element in that place 
        #         return True
        #     else: 
        #         #return the value o
        #         return False
    
    # def update_element(self, element_type, element_value, element_position, element_mode):
    #     # 
    #     if element_type == 'timer':
    #         #update timer  function 
    #         if self.checkCurrentElements(flag) == True:
    #             # update the element with the new value
    #             cv2.rectangle(self.frames('display'),(xTL, yTL), (xBR,yBR), (255,255,255),3) 
    #             cv2.putText(self.frames('display', value.tostring, ))
    #         else: 
    #             #create the element and then update it
    #             self.createElement(flag, value, position, mode)
    #             # display the value 

    #     elif element_type == 'keyboard':
    #         # display keyboard 
    #         pass

    #     elif element_type == 'target':
    #         # display target phrase? word??
    #         # TODO: try 
    #         pass

    #     elif element_type == 'leaderboard':
    #         # display leaderboard
    #         pass

    #     elif element_type == 'user input':
    #         # display the user key
    #         pass

    #     elif element_type == 'score':
    #         # display the score 
    #         #check the element flag, then do things based on the value of the flag 
    #         # 1 = keyboard
    #         # 2 = Target 
    #         # 3 = Timer
    #         pass

    def draw_keyboard(self, kb):
        # draws keyboard on the camera frame
        font = cv2.FONT_HERSHEY_COMPLEX
        def draw_key(kb, letter, frame=None):
            k_params = kb.get_key_params(letter)
            border_thickness = 3
            if kb.detector['active_key'] == letter:
                border_thickness = 12
            cv2.rectangle(frame, k_params['k_start_coords'], k_params['k_end_coords'], (255,255,255), border_thickness)
            cv2.putText(frame, letter, k_params['l_coords'], font, 0.5, (200,255,255), 1, cv2.LINE_AA)
        
        for row in range(kb.graphic['kb_shape'][0]):
            for col in range(kb.graphic['kb_shape'][1]):
                draw_key(kb, kb.layout[row][col], self.frames['camera'])


    def readElement(self, elementFlag, elementName):
        #check the element flag, then get the values of the element that is being asked 
        # TODO: How should I store the objects that are on the displa
        
        # the only elements that you will need to read will be keyboard -- its already detecting 
        #  
        return

    def combine_elements(self):
        pass