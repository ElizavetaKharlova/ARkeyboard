import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    retVal, frame = cap.read()
    imgray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # blur the image a bit
    imgray = cv2.GaussianBlur(imgray,(3,3),0)
    ret,thresh = cv2.threshold(imgray,60,255,0,cv2.THRESH_TOZERO)
    contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[:2]
    #print "contours looks like %r %r " % (contours[0],contours[1])

    #th2 = cv2.AdaptiveThreshold(frame,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
#            cv2.THRESH_BINARY,11,2)

    ctr = np.array(contours).reshape((-1,1,2)).astype(np.int32)

    #cv2.drawContours(frame, contours, -1, (0,255,0), 2)
    cv2.drawContours(thresh, [ctr], -1, (0, 255, 0), 2)
    cv2.imshow('frame', frame)
    #cv2.imshow('Adaptive thresh',th2)
    cv2.imshow('thresh',thresh)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
