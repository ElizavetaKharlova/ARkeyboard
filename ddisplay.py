import cv2 
import numpy as np
import ar_keyboard
import timer

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
                draw_key(kb, kb.layout[row][col], self.frames['display'])


    def draw_timer(self, rt):
        # boarder_thickness = 3
        start_location = (int(self.frames['display'].shape[1]*0.46), 80)
        # stop_location = (60, 100)
        font = cv2.FONT_HERSHEY_COMPLEX 
        # cv2.rectangle(frame, start_location,stop_location,(255,255,255), boarder_thickness)
        cv2.putText(self.frames['display'], rt, start_location,font, 3, (0, 0, 255), 1, cv2.LINE_AA)
    
    def draw_targets(self, game):
        next_char = game.targets[game.w_index]
        next_sentence = game.targets[game.w_index+1:game.w_index+25]
        start_location = (30, 70)
        font = cv2.FONT_HERSHEY_COMPLEX 
        cv2.putText(self.frames['display'], next_char+next_sentence, start_location,font, 1, (255, 255, 255), 1, cv2.LINE_AA)
    
    def draw_score(self, score):
        start_location = (int(self.frames['display'].shape[1]*0.85), 70)
        start_location_text = (int(self.frames['display'].shape[1]*0.75)-100, 70)
        font = cv2.FONT_HERSHEY_COMPLEX
        cv2.putText(self.frames['display'], "Your score:", start_location_text,font, 1, (255, 255, 255), 1, cv2.LINE_AA)
        # cv2.rectangle(frame, start_location,stop_location,(255,255,255), boarder_thickness)
        cv2.putText(self.frames['display'], str(score), start_location,font, 2, (255, 255, 255), 1, cv2.LINE_AA)
        

    def combine_elements(self):
        pass
