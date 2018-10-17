import ar_keyboard
import cv2
import numpy as np
import matplotlib
import math

kb_layout = (('Q','W','E','R','T','Y','U','I','O','P'),
             ('A','S','D','F','G','H','J','K','L','.'),
             ('Z','X','C','V','B','N','M',' ','!','?'))

kb = ar_keyboard.Keyboard()


cap = cv2.VideoCapture(0)
ret, video_frame = cap.read()
kb.init_kb_params(kb_layout, video_frame)



while True:
    # Capture and process the frame
    ret, image = cap.read()
    img = image.copy()
    img = cv2.flip(img,1)
    det = img.copy()
    font = cv2.FONT_HERSHEY_COMPLEX

    # Draw keyboard
    # for row in range(kb_params[4][0]):
    #     for col in range(kb_params[4][1]):
    #         put_button(kb_layout, kb_layout[row][col], kb_params, frames)
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
    active_key = kb.detect_key(det)
    print(active_key)
    cv2.imshow('img',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()