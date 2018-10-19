# import the necessary packages
import imutils
import numpy as np
import argparse
import cv2
import matplotlib


class Calibratus_rex(object):
    
    def __init__(self,image_1, image_2,):#could also have other arguments in here for initializing)
        self.first_im= image_1
        self.second_im = image_2

    def config_button(image_1,image_2):
     cv2.rectangle(image_1,(900,100), (950,150), (255,255,255), 3)
     cv2.rectangle(image_2,(900,100), (950,150), (255,255,255), 3)
    
    def Get_pixle_value(HSV_image):
    #this is the function to return your hsv value 
        while True: 
        #this is where we sample the pixel 
            self.HSV_calc=HSV_image[925,125]
            print("the pixel value is:",self.HSV_calc)
        #pressing e will terminate the aquisition 
            if cv2.waitKey(1) & 0xFF == ord('e'):
                break
    
    def Give_pixle_val(self):
        val = self.HSV_calc
        return val
    
        #i should probably get rid of the rectangles now 

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video",
        help = "path to the (optional) video file")
args = vars(ap.parse_args())

# define the upper and lower boundaries of the HSV pixel
# intensities to be considered 'skin'
lower = np.array([0, 48, 80], dtype = "uint8")
upper = np.array([20, 255, 255], dtype = "uint8")

#if a video path was not supplied, grab the reference
# to the gray
if not args.get("video", False):
 camera = cv2.VideoCapture(0)

# otherwise, load the video
else:
 camera = cv2.VideoCapture(args["video"])
 # keep looping over the frames in the video
while True:
	# grab the current frame
	(grabbed, frame) = camera.read()
        
	# if we are viewing a video and we did not grab a
	# frame, then we have reached the end of the video
	if args.get("video") and not grabbed:
		break

	# resize the frame, convert it to the HSV color space,
	# and determine the HSV pixel intensities that fall into
	# the speicifed upper and lower boundaries
	frame = imutils.resize(frame, width = 400)
	converted = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	#This is where I need to put in my calibration module
        #summon a Calibratus_rex
        calibrator=Calibratus_rex(frame,converted)
        calibrator.config_button
        cal_val=calibrator.

        
        skinMask = cv2.inRange(converted, lower, upper)

	# apply a series of erosions and dilations to the mask
	# using an elliptical kernel
	kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
	skinMask = cv2.erode(skinMask, kernel, iterations = 2)
	skinMask = cv2.dilate(skinMask, kernel, iterations = 2)

	# blur the mask to help remove noise, then apply the
	# mask to the frame
	skinMask = cv2.GaussianBlur(skinMask, (3, 3), 0)
	skin = cv2.bitwise_and(frame, frame, mask = skinMask)

	# show the skin in the image along with the mask
	#cv2.imshow("images", np.hstack([frame, skin]))
        cv2.imshow(converted)
	# if the 'q' key is pressed, stop the loop
	if cv2.waitKey(1) & 0xFF == ord("q"):
		break

# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
