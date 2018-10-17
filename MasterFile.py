#This master file will feature 3 modes:
#-----------------------------------------------------------------------------------------------------------------------
# Mode Rest:
#  calls the 'getLeaderboard' function, displays a leaderboard,
#  Displays a prompt to onboard by pressing space,
#  Displays the option to terminate by pressing escape
#-----------------------------------------------------------------------------------------------------------------------
# Mode Onboard:
#  displays and calls the keyboard
#  prompts to type ur name by using the keyboard
#  promts to use space to start Game
#  prompts to use escape to return to Rest
#-----------------------------------------------------------------------------------------------------------------------
# Mode Game:
# calls the "getTarget"function, displays the target
# calls the 'getKeyTyped' function and displays the sequence typed
# calls the 'getAccuracy' function and displays the accuracy
# calls the 'getTimer' function and displays the Time
# prompts to quit by using escape


## Imports:
import keyboard #Using module keyboard ... THIS IS NOT THE VIRTUALKEYBOARD
import numpy as np
# import HandleDisplayThings # handles OPENCV stuff and the displaying
import ar_keyboard # this is the virtual keyboard
import keyboard_ar as getKeyboardOutput # this is the virtual keyboard
import timerClass as GetTimer
from getScore import getDistance
# import getTargetWord

kb_layout = (('Q','W','E','R','T','Y','U','I','O','P'),
             ('A','S','D','F','G','H','J','K','L','.'),
             ('Z','X','C','V','B','N','M',' ','!','?'))

#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------GAME MODE---------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
def runGameMode(player_name, Keyboard, target, Display):
    # run the while loop while the time
    Timer = GetTimer
    time_rest = Timer.getRemainingTime
    typed_word = ''
    score = 0
    while time_rest > 0:
        time_rest = Timer.getRemainingTime
        Display.updateElement(time_rest, flag='time_remaining', mode='play')
        Display.update(target, flag='Target')

        video_frame = Display.get_frame()
        letter = Keyboard.detect_key(video_frame['detection'])
        if letter is not None:
            typed_word = typed_word + letter
            index = min(len(typed_word), len(target))
            score = getDistance(typed_word[index], target[index])

        Display.updateElement(typed_word, flag='typed_word', mode='play')
        Display.updateElement(score, flag='score', mode='play')

    return score, time_rest
#-----------------------------------------------------------------------------------------------------------------------
#--------------------------------------------ONBOARDING MODE------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
def runOnboardingMode(Display):
    # the loop eits if we click escape, that means we go back to RestMode
    print('Press ESC in order to quit Onboarding')
    print('enter yout player Name,')
    print('after you have entered, please press ENTER on the normal keyboard to proccees ')

    # Initialize the Keyboard, initialize the PlayerName, prompt player to write their name
    Keyboard = ar_keyboard.Keyboard()
    #Display.getframe()
    # frame in this format:
    # ret, video_frame = cap.read()
    video_frame = Display.get_frame()
    Keyboard.init_kb_params(kb_layout, video_frame['detection'])
    player_name = ''
    score = np.nan
    time_taken = np.nan
    greeting_printed = False

    # after name is written, loop terminates pressing Enter on the main keyboard
    while keyboard.is_pressed('esc') != True:

        # get to enter Name
        while keyboard.is_pressed('enter') != True:
            try:
                # get letter from Keyboard
                # pass in video frame
                video_frame = Display.get_frame()
                letter = Keyboard.detect_key(video_frame['detection'])
                if letter == None:
                    pass
                else:
                    player_name = player_name + letter
                    Display.update(player_name, flag='PlayerName', mode='register')
            except:
                pass

        # If we have a Player name and he has not been greeted yet, then do so!
        if (greeting_printed == False) & (player_name is not ''):
            print('Welcome, ', player_name, '!')

        print('Get ready for the Game to start!')
        target = getTargetWord
        score, time_taken = runGameMode(player_name, Keyboard, target, Display)
        return player_name, score, time_taken
    return player_name, score, time_taken
#-----------------------------------------------------------------------------------------------------------------------
#--------------------------------------RESTING MODE---------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
# This is also the main loop
pastPerformance_dict = {'Name': 'Noone yet',
                        'Score': -99999,
                        'Time': 99999}
Display = HandleDisplayThings
while keyboard.is_pressed('esc') != True:
    print('Press ESC in order to quit completely')

    # update the leaderboard, display new leaderboard
    Display.update(pastPerformance_dict, flag='Leaderboard')

    try: #used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('space'):  # if key 'space' is pressed
            print('You pressed space!')
            print('We wll get need you to register first :-)')
            player_name, score, time_taken = runOnboardingMode(Display)
        else:
            pass
    except:
        pass



#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------GAME MODE---------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------



