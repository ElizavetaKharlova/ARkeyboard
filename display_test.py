import cv2
import ddisplay
import ar_keyboard
import timer
import game

disp = ddisplay.Display()
timer = timer.Timer()
disp.read_camera()
game = game.Game()

kb_layout = (('Q','W','E','R','T','Y','U','I','O','P'),
             ('A','S','D','F','G','H','J','K','L','.'),
             ('Z','X','C','V','B','N','M',' ','!','?'))
kb = ar_keyboard.Keyboard()
kb.init_kb_params(kb_layout, disp.frames['detection'])

last_active_key = None

score = 0
targets = game.get_next()

while True:
    disp.read_camera()
    kb.detect_key(disp.frames['detection'])
    active_key = kb.detector['active_key']
    remaining_time = max(0, timer.getRemainingTime())

    if active_key != last_active_key:
        last_active_key = active_key
        if active_key is not None:
            if active_key.lower() != targets['letter'].lower():
                pass
            else:
                targets = game.get_next()
                if remaining_time >= 0:
                    score += 1
                    # print(active_key, score)

    # print(timer.getRemainingTime())

    disp.draw_keyboard(kb)
    disp.draw_targets(game)
    disp.draw_timer(str(remaining_time))
    disp.draw_score(score)

    cv2.imshow('camera',disp.frames['display'])
    # cv2.imshow('display',disp.frames['display'])
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
del disp