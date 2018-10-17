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
<<<<<<< HEAD
import keyboard #Using module keyboard ... THIS IS NOT THE VIRTUALKEYBOARD
import HandleDisplayThings # handles OPENCV stuff and the displaying
import getKeyboardOutput # this is the virtual keyboard
import getTargetWord
import getScore
=======
import keyboard #Using module keyboard

>>>>>>> parent of a1a2cfc... Updated MasterFile followup


#-----------------------------------------------------------------------------------------------------------------------
#--------------------------------------RESTING MODE---------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
# This is also the main loop
while keyboard.is_pressed('esc') != True:
    print('Press ESC in order to quit completely')

    # update the leaderboard, display new leaderboard
    Leaderboard = getLeaderboard(pastPerformance_dict)
    Leaderboard.display

    try: #used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('space'):  # if key 'space' is pressed
            print('You pressed space!')
            print('We wll get need you to register first :-)')
            PlayerName, Score, Time = runOnboardingMode()
        else:
            pass
    except:
        pass

#-----------------------------------------------------------------------------------------------------------------------
#--------------------------------------------ONBOARDING MODE------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
def runOnboardingMode():
    # the loop eits if we click escape, that means we go back to RestMode
    print('Press ESC in order to quit Onboarding')
    print('enter yout player Name,')
    print('after you have entered, please press ENTER on the normal keyboard to proccees ')

    # Initialize the Keyboard, initialize the PlayerName, prompt player to write their name
    Keyboard = getKeyboardOutput(Display)
    PlayerName = ''
    Score = nan
    Time = nan
    GreetingPrinted = False

    # after name is written, loop terminates pressing Enter on the main keyboard
    while keyboard.is_pressed('esc') != True:

        # get to enter Name
        while keyboard.is_pressed('enter') != True:
            try:
                # get letter from Keyboard
                letter = Keyboard.read()
                if letter == None:
                    pass
                else:
                    PlayerName = PlayerName + letter
                    Display.update(PlayerName, flag='PlayerName')
            except:
                pass

        # If we have a Player name and he has not been greeted yet, then do so!
        if (GreetingPrinted == False) & (Playername is not ''):
            print('Welcome, ', PlayerName, '!')

        print('Get ready for the Game to start!')
        Target = getTargetWord
        Score, Time = runGameMode(PlayerName, Keyboard, Target)
        return PlayerName, Score, Time
    return PlayerName, Score, Time
#-----------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------GAME MODE---------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------
def runGameMode(PlayerName, Keyboard, Target, Display):
    # run the while loop while the time
    Timer = getTimer
    Time = Timer.gettime
    TypedWord = ''
    Score = 0
    while Timer > 0:
        Time = Timer.gettime
        Display.update(Time, flag='TimeRemaining')
        Display.update(Target, flag='Target')

        letter = Keyboard.read(Display)
        if letter is not none:
            TypedWord = TypedWord + letter
            Score = getScore(TypedWord, Target)

        Display.update(TypedWord, flag='TypedWord')
        Display.update(Score, flag='Score')

    return Score, Time


pastPerformance_dict = {'Name': 'Noone yet',
                        'Score': -99999,
                        'Time': 99999}

