
qwertyKeyboardArray = [
    ['`','1','2','3','4','5','6','7','8','9','0','-','='],
    ['q','w','e','r','t','y','u','i','o','p','[',']','\\'],
    ['a','s','d','f','g','h','j','k','l',';','\''],
    ['z','x','c','v','b','n','m',',','.','/'],
    ['', '', ' ', ' ', ' ', ' ', ' ', '', '']
    ]

qwertyShiftedKeyboardArray = [
    ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '+'],
    ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}', '|'],
    ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ':', '"'],
    ['Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?'],
    ['', '', ' ', ' ', ' ', ' ', ' ', '', '']
    ]

layoutDict = {'QWERTY': (qwertyKeyboardArray, qwertyShiftedKeyboardArray)}

# Sets the default keyboard to use to be QWERTY.
keyboardArray = qwertyKeyboardArray
shiftedKeyboardArray = qwertyShiftedKeyboardArray

# Returns the keyboard layout c "lives in"; for instance, if c is A, this will
# return the shifted keyboard array, but if it is a, it will return the regular
# keyboard array.  Raises a ValueError if character is in neither array
def arrayForChar(c):
    if (True in [c in r for r in keyboardArray]):
        return keyboardArray
    elif (True in [c in r for r in shiftedKeyboardArray]):
        return shiftedKeyboardArray
    else:
        raise ValueError(c + " not found in any keyboard layouts")

# Finds a 2-tuple representing c's position on the given keyboard array.  If
# the character is not in the given array, throws a ValueError
def getCharacterCoord(c, array):
    row = -1
    column = -1
    for r in array:
        if c in r:
            row = array.index(r)
            column = r.index(c)
            return (row, column)
    raise ValueError(c + " not found in given keyboard layout")

# Finds the Euclidean distance between two characters, regardless of whether
# they're shifted or not.
def getDistance(c1, c2):
    coord1 = getCharacterCoord(c1, arrayForChar(c1))
    coord2 = getCharacterCoord(c2, arrayForChar(c2))
    return ((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)**(0.5)
