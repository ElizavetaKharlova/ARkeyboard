# this is to try some edge detection
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    retVal, frame = cap.read()
    imgray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # blur the image a bit
    imgray = cv2.GaussianBlur(imgray,(3,3),0)

    laplacian = cv2.Laplacian(imgray,cv2.CV_64F)

    cv2.imshow("Grey", imgray)
    cv2.imshow("laplacian", laplacian)

    if cv2.waitKey(1) & 0xFF == ord('q'):
          break

cap.release()
cv2.destroyAllWindows()
