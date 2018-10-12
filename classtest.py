import cv2
import numpy as np

from elements import keyboard


cap = cv2.VideoCapture(0)


while True:
    # Capture and process the frame
    ret, image = cap.read()
    img = image.copy()
    img = cv2.flip(img,1)
    gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret1, thresh = cv2.threshold(gray, 115, 255, cv2.THRESH_BINARY)
    kernel = np.ones((3,3),np.uint8)
    opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN, kernel, iterations = 3)

    key = keyboard(img)
    key.display(img, 0, 0)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    cap.release()