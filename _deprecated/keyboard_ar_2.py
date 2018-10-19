import cv2
import numpy as np
import matplotlib
import math

kb_layout = (('Q','W','E','R','T','Y','U','I','O','P'),
             ('A','S','D','F','G','H','J','K','L','.'),
             ('Z','X','C','V','B','N','M',' ','!','?'))

def determine_kb_location(kb_layout):
    cap = cv2.VideoCapture(0)
    kb_shape = np.shape(kb_layout)
    ret, video_frame = cap.read()
    feed_height, feed_width, feed_channels = video_frame.shape

    key_dim_h = math.floor(feed_width/(kb_shape[1]+2))
    key_dim_v = key_dim_h

    kb_starting_position_x = math.floor((feed_width - (key_dim_h * kb_shape[1]))/2)
    kb_starting_position_y = math.floor((feed_height - (key_dim_v * kb_shape[0]))/2)
    cap.release()
    
    return kb_starting_position_x, kb_starting_position_y, key_dim_h, key_dim_v, kb_shape

def find_letter_index(kb_layout, letter):
    ind = np.where(np.array(kb_layout) ==letter)
    return ind[0][0], ind[1][0]

def put_button(kb_layout, letter, kb_params=None, frames=None):
    if kb_params is None:
        return False
    if frames is None or type(frames) is not dict:
        return False
    letter_index = find_letter_index(kb_layout, letter)
    key_start_x = kb_params[0] + letter_index[1] * kb_params[2]
    key_start_y = kb_params[1] + letter_index[0] * kb_params[3]

    key_end_x = key_start_x + kb_params[2]
    key_end_y = key_start_y + kb_params[3]

    cv2.rectangle(frames['c'], (key_start_x, key_start_y), (key_end_x, key_end_y), (255,255,255), 3)
    cv2.putText(frames['c'], letter, (key_start_x + math.floor(kb_params[2]/2), key_start_y + math.floor(kb_params[3]/2)), font, 0.5, (200,255,255), 1, cv2.LINE_AA)


def which_key_pressed(kb_layout, kb_params=None, frames=None):
    # step 1: slice keys
    detection_factors = {}
    for letter in ('Q','W','E','R','T','Y','U','I','O','P', 'A','S','D','F','G','H','J','K','L','.','Z','X','C','V','B','N','M',' ','!','?'):
        letter_index = find_letter_index(kb_layout, letter)
        key_start_x = kb_params[0] + letter_index[1] * kb_params[2]
        key_start_y = kb_params[1] + letter_index[0] * kb_params[3]
        key_end_x = key_start_x + kb_params[2]
        key_end_y = key_start_y + kb_params[3]
        key_slice = frames['diet'][key_start_y:key_end_y, key_start_x:key_end_x]

        # step 2: find out how much orange is in the key slice
        hsv = cv2.cvtColor(key_slice, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, (65, 60, 60), (80, 255, 255))
        detection_factor = cv2.countNonZero(mask) / (kb_params[2] * kb_params[3])
        detection_factors[letter] = detection_factor

    # rank keys
        keys_ranked = sorted(detection_factors, key=detection_factors.get, reverse=True)

    # step 4: highest ranked key is the key
    return keys_ranked[0]

kb_params = determine_kb_location(kb_layout)
cap = cv2.VideoCapture(0)

while True:
    # Capture and process the frame
    ret, image = cap.read()
    img = image.copy()
    img = cv2.flip(img,1)
    det = img.copy()
    font = cv2.FONT_HERSHEY_COMPLEX

    frames = {
        'diet': det,
        'c': img
        }

    # Draw keyboard
    for row in range(kb_params[4][0]):
        for col in range(kb_params[4][1]):
            put_button(kb_layout, kb_layout[row][col], kb_params, frames)
#
#     # Wait for a 25-frame delay and add the new key to the output
#     lettr = is_it_pressed()
#     # checks pixle values based on the thresholding algorithm
#     if not lettr == '0':
#         i = i + 1
#         if (i > 25):
#             type_word = type_word + lettr
#             if len(type_word) > 15:
#                 type_word = ' '
#             i = 0
#  #this is wheere the text gets displayed
#     cv2.putText(img, type_word, (900,300), font, 1, (200,255,255), 2, cv2.LINE_AA)
#
    key_slice = which_key_pressed(kb_layout, kb_params, frames)
    print(key_slice)
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
