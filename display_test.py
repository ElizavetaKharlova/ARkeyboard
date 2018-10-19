
import cv2
import display
import ar_keyboard

disp = display.Display()
disp.read_camera()

kb_layout = (('Q','W','E','R','T','Y','U','I','O','P'),
             ('A','S','D','F','G','H','J','K','L','.'),
             ('Z','X','C','V','B','N','M',' ','!','?'))
kb = ar_keyboard.Keyboard()
kb.init_kb_params(kb_layout, disp.frames['detection'])

while True:
    disp.read_camera()
    kb.detect_key(disp.frames['detection'])

    disp.draw_keyboard(kb)

    cv2.imshow('camera',disp.frames['camera'])
    cv2.imshow('display',disp.frames['display'])
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
del disp