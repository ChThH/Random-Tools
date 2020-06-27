import random

def dice(num,max=6):
    '''Rolls num(ber) of max(imum) sided dice'''
    rolls = list()
    for each in range(num):
        # print(each)
        rolls.append(random.randint(1,max))
    return rolls

def dice_string(num,max=6):
    '''Creates a string of dice rolls useful for dicewords'''
    rolls = ''
    for each in range(num):
        if (each != 0 and each % 5 == 0):
            rolls += ':'
        rolls += str(random.randint(1,max))
    return rolls