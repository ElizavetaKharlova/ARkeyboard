# this
import cv2

import numpy as np

class keyboard():

    '''
This class generates a keyboard on the screen at the x and y Pixel locations
'''

    def __init__(self, frame):
        self.frame = frame
        self.pixelSpacing = 50
        self.font = cv2.FONT_HERSHEY_COMPLEX
        # these are used to check if the keys have been pressed.
        self.arr1 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.arr2 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.arr3 = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        self.arr_let1 = ('Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P')
        self.arr_let2 = ('A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', '.')
        self.arr_let3 = ('Z', 'X', 'C', 'V', 'B', 'N', 'M', ' ', '!', '?')


    # THESE VALUES DEFINE THE middle LOCATIONS
    start_key = (900, 100) # this is actually the middle
    finish_key = (950, 150)



    # this creates the arrays and the letters for the grid


    def put_button(hor, vert, letter):
        cv2.rectangle(opening, (start_key[0] + hor * pixelSpacing, start_key[1] + vert * pixelSpacing),
                      (finish_key[0] + hor * pixelSpacing, finish_key[1] + vert * 50), (255, 255, 255), 3)
        cv2.putText(opening, letter, (start_key[0] + 20 + hor * 50, start_key[1] + 20 + vert * 50), font, 0.5,
                    (200, 255, 255), 1, cv2.LINE_AA)

        # Draw a button on the colour frame

    def put_button_color(hor, vert, letter):
        cv2.rectangle(img, (start_key[0] + hor * 50, start_key[1] + vert * 50),
                      (finish_key[0] + hor * 50, finish_key[1] + vert * 50), (255, 255, 255), 3)
        cv2.putText(img, letter, (start_key[0] + 20 + hor * 50, start_key[1] + 20 + vert * 50), font, 0.5,
                    (200, 255, 255), 1, cv2.LINE_AA)

    def display(self, x, y):
       """

       :param frame: this is the frame that the element will be displayed on
       :param x: This is the x pixel for the top right of the element
       :param y: This is the y pixel for the top right of the element
       :return:
       """

        self.put_button(-4, 0, 'Q')
        self.put_button(-3, 0, 'W')
        self.put_button(-2, 0, 'E')
        self.put_button(-1, 0, 'R')
        self.put_button(0, 0, 'T')
        self.put_button(1, 0, 'Y')
        self.put_button(2, 0, 'U')
        self.put_button(3, 0, 'I')
        self.put_button(4, 0, 'O')
        self.put_button(5, 0, 'P')

        self.put_button(-4, 1, 'A')
        self.put_button(-3, 1, 'S')
        self.put_button(-2, 1, 'D')
        self.put_button(-1, 1, 'F')
        self.put_button(0, 1, 'G')
        self.put_button(1, 1, 'H')
        self.put_button(2, 1, 'J')
        self.put_button(3, 1, 'K')
        self.put_button(4, 1, 'L')

        self.put_button(-4, 2, 'Z')
        self.put_button(-3, 2, 'X')
        self.put_button(-2, 2, 'C')
        self.put_button(-1, 2, 'V')
        self.put_button(0, 2, 'B')
        self.put_button(1, 2, 'N')
        self.put_button(2, 2, 'M')
        self.put_button(3, 2, ' ')
        self.put_button(4, 2, '!')

class timer():

    def display(self, x, y):
        '''

        :param x:
        :param y:
        :return:
        '''
class targetDisplay():
    '''

    '''

    def display(self, x, y):
        '''

        :param x:
        :param y:
        :return:
        '''
class leaderboard():
    '''


    '''
    def display(self, x, y):
        '''

        :param x:
        :param y:
        :return:
        '''
