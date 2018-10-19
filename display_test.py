import cv2
import display
import ar_keyboard
import timer

disp = display.Display()
timer = timer.Timer()
disp.read_camera()

kb_layout = (('Q','W','E','R','T','Y','U','I','O','P'),
             ('A','S','D','F','G','H','J','K','L','.'),
             ('Z','X','C','V','B','N','M',' ','!','?'))
kb = ar_keyboard.Keyboard()
kb.init_kb_params(kb_layout, disp.frames['detection'])

last_active_key = None

while True:
    disp.read_camera()
    kb.detect_key(disp.frames['detection'])

    active_key = kb.detector['active_key']

    if active_key != last_active_key:
        last_active_key = active_key
        if active_key is not None:
            print(active_key)

    # print(timer.getRemainingTime())

    disp.draw_keyboard(kb)
    disp.draw_timer(str(timer.getRemainingTime()))

    cv2.imshow('camera',disp.frames['display'])
    # cv2.imshow('display',disp.frames['display'])
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
del disp