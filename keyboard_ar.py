import cv2
import numpy as np
import matplotlib

cap = cv2.VideoCapture(0)
type_word = ' '
i = 0
start_key = (900, 100)
finish_key = (950,150)
arr1 = (0,1,2,3,4,5,6,7,8,9)
arr2 = (0,1,2,3,4,5,6,7,8,9)
arr3 = (0,1,2,3,4,5,6,7,8,9)
arr_let1 = ('Q','W','E','R','T','Y','U','I','O','P')
arr_let2 = ('A','S','D','F','G','H','J','K','L','.')
arr_let3 = ('Z','X','C','V','B','N','M',' ','!','?')

while True:
    # Capture and process the frame
    ret, image = cap.read()
    img = image.copy()
    img = cv2.flip(img,1)
    gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret1, thresh = cv2.threshold(gray, 115, 255, cv2.THRESH_BINARY)
    kernel = np.ones((3,3),np.uint8)
    opening = cv2.morphologyEx(thresh,cv2.MORPH_OPEN, kernel, iterations = 3)
    font = cv2.FONT_HERSHEY_COMPLEX
    
    # Draw a button on the threshlod frame
    def put_button(hor, vert, letter):
        cv2.rectangle(opening, (start_key[0]+hor*50,start_key[1]+vert*50), (finish_key[0]+hor*50,finish_key[1]+vert*50), (255,255,255), 3)
        cv2.putText(opening, letter, (start_key[0]+20+hor*50,start_key[1]+20+vert*50), font, 0.5, (200,255,255), 1, cv2.LINE_AA)
    
    # Draw a button on the colour frame
    def put_button_color(hor,vert,letter):
        cv2.rectangle(img, (start_key[0]+hor*50,start_key[1]+vert*50), (finish_key[0]+hor*50,finish_key[1]+vert*50), (255,255,255), 3)
        cv2.putText(img, letter, (start_key[0]+20+hor*50,start_key[1]+20+vert*50), font, 0.5, (200,255,255), 1, cv2.LINE_AA)

    # Check which button is pressed
    def is_it_pressed():
        let = '0'
        for k in (1,2,3):
            if k == 1:
                for i in arr3:
                    if np.all(opening[225,725+i*50] != [0,0,0]):
                        let = arr_let3[i]
            if k == 2:
                for i in arr2:
                    if np.all(opening[175,725+i*50] != [0,0,0]):
                        let = arr_let2[i]
            if k == 3:
                for i in arr1:
                    if np.all(opening[125,725+i*50] != [0,0,0]):
                        let = arr_let1[i]

        return let
    # Draw a grid on the threshold frame
    put_button(-4,0,'Q')
    put_button(-3,0,'W')
    put_button(-2,0,'E')
    put_button(-1,0,'R')
    put_button(0,0,'T')
    put_button(1,0,'Y')
    put_button(2,0,'U')
    put_button(3,0,'I')
    put_button(4,0,'O')
    put_button(5,0,'P')

    put_button(-4,1,'A')
    put_button(-3,1,'S')
    put_button(-2,1,'D')
    put_button(-1,1,'F')
    put_button(0,1,'G')
    put_button(1,1,'H')
    put_button(2,1,'J')
    put_button(3,1,'K')
    put_button(4,1,'L')
    
    put_button(-4,2,'Z')
    put_button(-3,2,'X')
    put_button(-2,2,'C')
    put_button(-1,2,'V')
    put_button(0,2,'B')
    put_button(1,2,'N')
    put_button(2,2,'M')
    put_button(3,2,' ')
    put_button(4,2,'!')
    
    # Draw a grid on the colour frame
    put_button_color(-4,0,'Q')
    put_button_color(-3,0,'W')
    put_button_color(-2,0,'E')
    put_button_color(-1,0,'R')
    put_button_color(0,0,'T')
    put_button_color(1,0,'Y')
    put_button_color(2,0,'U')
    put_button_color(3,0,'I')
    put_button_color(4,0,'O')
    put_button_color(5,0,'P')

    put_button_color(-4,1,'A')
    put_button_color(-3,1,'S')
    put_button_color(-2,1,'D')
    put_button_color(-1,1,'F')
    put_button_color(0,1,'G')
    put_button_color(1,1,'H')
    put_button_color(2,1,'J')
    put_button_color(3,1,'K')
    put_button_color(4,1,'L')
    put_button_color(5,1,'.')
    
    put_button_color(-4,2,'Z')
    put_button_color(-3,2,'X')
    put_button_color(-2,2,'C')
    put_button_color(-1,2,'V')
    put_button_color(0,2,'B')
    put_button_color(1,2,'N')
    put_button_color(2,2,'M')
    put_button_color(3,2,' ')
    put_button_color(4,2,'!')
    put_button_color(5,2,'?')

    # Wait for a 25-frame delay and add the new key to the output
    lettr = is_it_pressed()
    if not lettr == '0':
        i = i + 1
        if (i > 25):
            type_word = type_word + lettr
            if len(type_word) > 15:
                type_word = ' '
            i = 0
    
    cv2.putText(img, type_word, (900,300), font, 1, (200,255,255), 2, cv2.LINE_AA)

    if not np.all(opening[125,1215] == [0,0,0]):
        cv2.putText(img, 'Fuck you', (900,500), font, 1, (100,100,100), 2, cv2.LINE_AA)
        
    cv2.imshow('img',img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
