import cv2
import numpy as np
import matplotlib
import math

kb_layout = (('Q','W','E','R','T','Y','U','I','O','P'),
             ('A','S','D','F','G','H','J','K','L','.'),
             ('Z','X','C','V','B','N','M',' ','!','?'))

def Keyboard():
    def __init__(self):
        self.layout = None
        self.layout_flat = ('Q','W','E','R','T','Y','U','I','O','P', 'A','S','D','F','G','H','J','K','L','.','Z','X','C','V','B','N','M',' ','!','?')
        self.graphic = {
            'kb_shape': None,
            'kb_start_x': None,
            'kb_start_y': None,
            'k_dim_h': None,
            'k_dim_v': None
        }
        self.detector {
            'active_key': None,
            'persistency': 0,
            'threshold': 12
        }

    def init_kb_params(self, layout, video_cap_frame):
        feed_height, feed_width = video_cap_frame.shape

        kb_shape = np.shape(kb_layout)
        k_dim_h = math.floor(feed_width/(kb_shape[1]+2))
        k_dim_v = k_dim_h

        self.graphic['kb_shape'] = kb_shape
        self.graphic['k_dim_h'] = k_dim_h
        self.graphic['k_dim_v'] = k_dim_v
        self.graphic['kb_start_x'] = math.floor((feed_width - (k_dim_h * kb_shape[1]))/2)
        self.graphic['kb_start_y'] = math.floor((feed_height - (k_dim_v * kb_shape[0]))/2)
        
    def get_key_params(self, letter):
        ind = np.where(np.array(self.layout) ==letter)
        key_index = ind[0][0], ind[1][0]
        key_start_x = self.graphic['kb_start_x'] + key_index[1] * self.graphic['k_dim_h']
        key_start_y = self.graphic['kb_start_y'] + key_index[0] * self.graphic['k_dim_v']
        key_end_x = key_start_x + self.graphic['k_dim_h']
        key_end_y = key_start_y + self.graphic['k_dim_v']

        return {
            'key_index': key_index,
            'k_start_coords': (key_start_x, key_start_y)
            'k_end_coords': (key_end_x, key_end_y)
            'l_coords': (math.floor(key_start_x + self.graphic['k_dim_h']/2), 
                         math.floor(key_start_y + self.graphic['k_dim_v']/2))
        }

    def detect_key(self, frame):
        detection_factors = {}
        for letter in self.layout_flat:
            key_params = self.get_key_params(letter)
            key_start_x = key_params['k_start_coords'][0]
            key_start_y = key_params['k_start_coords'][1]
            key_end_x = key_params['k_end_coords'][0]
            key_end_y = key_params['k_end_coords'][1]
            key_slice = frame[key_start_y:key_end_y, key_start_x:key_end_x]

            # step 2: find out how much orange is in the key slice
            hsv = cv2.cvtColor(key_slice, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, (65, 60, 60), (80, 255, 255))
            detection_factor = cv2.countNonZero(mask) / (kb_params[2] * kb_params[3])
            detection_factors[letter] = detection_factor

        # step 3: rank keys
        keys_ranked = sorted(detection_factors, key=detection_factors.get, reverse=True)

        # step 4: highest ranked key is the key
        active_key = keys_ranked[0]
        if self.detector['active_key'] == active_key:
            self.detector['persistency'] += 1
        else:
            self.detector['active_key'] = active_key
            self.detector['persistency'] = 0

        if self.detector['persistency'] >= self.detector['threshold']:
            self.detector['persistency'] = 0
            return self.detector['active_key']
        else return None
