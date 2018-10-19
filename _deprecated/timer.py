import cv2
import sys
from datetime import datetime
import numpy as np

# Initialize variables
camSource = -1
running = True
saveCount = 0
nSecond = 0
totalSec = 30
#strSec = range(30)
#result = np.array(31)
#for i in range(31):
#    result[i] = str(i)
strSec = ['30', '29', '28', '27', '26','25','24','23','22','21','20','19','18','17','16','15','14','13','12','11','10','9','8','7','6','5','4','3','2','1']

keyPressTime = 0.0
startTime = 0.0
timeElapsed = 0.0
startCounter = False
endCounter = False

# Start the camera
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    sys.exit('Camera did not provide frame.')

frameWidth = 1280 # int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
frameHeight = 720 # int(cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))

# Start video stream
while running:
    ret, image = cap.read()
    img = image.copy()
    img = cv2.flip(img,1)
    
    # Display counter on screen before saving a frame
    if startCounter:
        if nSecond < totalSec:
            # draw the Nth second on each frame
            # till one second passes
            cv2.putText(img = img,
                        text = strSec[nSecond],
                        org = (int(frameWidth/2 - 20),int(frameHeight/2)),
                        fontFace = cv2.FONT_HERSHEY_DUPLEX,
                        fontScale = 6,
                        color = (255,255,255),
                        thickness = 5,
                        lineType = cv2.LINE_AA)
                
            timeElapsed = (datetime.now() - startTime).total_seconds()
#            print('timeElapsed: {}'.format(timeElapsed))

            if timeElapsed >= 1:
                nSecond += 1
#                print('nthSec:{}'.format(nSecond))
                timeElapsed = 0
                startTime = datetime.now()

        else:
            cv2.imwrite('img' + str(saveCount) + '.jpg', img)
            #            print 'saveTime: {}'.format(datetime.now() - keyPressTime)
            
            saveCount += 1
            startCounter = False
            nSecond = 1

    # Get user input
    keyPressed = cv2.waitKey(3)
    if keyPressed == ord('s'):
        startCounter = True
        startTime = datetime.now()
        keyPressTime = datetime.now()
        #        print 'startTime: {}'.format(startTime)
        #        print 'keyPressTime: {}'.format(keyPressTime)

    elif keyPressed == ord('q'):
        # Quit the while loop
        running = False
        cv2.destroyAllWindows()

        # Show video stream in a window
    cv2.imshow('video', img)

cap.release()
