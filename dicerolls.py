import random
import argparse
import sys


def dice(num, sides=6, fun=True):
    '''Rolls a num(ber) of varible sided dice'''
    try:
        if fun == True:
            if num % 1 != 0:
                msg = 'I\'m not rolling a fractional die for anyone.'
                raise(ValueError)
            elif sides % 1 != 0:
                msg = 'Seriously, I can\'t roll dice with fractional sides; what would that even mean?'
                raise (ValueError)
            elif num == 0:
                msg = 'So you don\'t want to roll any dice.'
                raise (ValueError)
            elif num < 0:
                msg = 'Negative numbers, huh? \nOkay, you roll the dice then. Let me know how it goes.'
                raise (ValueError)
            elif sides < 1:
                msg = "I see you're unfamiliar with dice. Dice must have at least one side."
                raise (ValueError)
            elif num == 1 and sides == 1:
                print('What\'s the point of rolling a 1-sided die?')
            elif num == 1 and sides == 2:
                print('So you\'re flipping a coin.')
            elif sides == 1:
                print('What\'s the point of rolling 1-sided dice?')
            elif sides == 2:
                print('Let the coin flipping begin!')
        else:
            if num < 1 or num % 1 != 0:
                msg = 'Number of dice invalid.'
                raise(ValueError)
            elif sides % 1 != 0 or sides < 1:
                msg = 'Sides of dice invalid.'
                raise(ValueError)
    except(ValueError):
        print(msg)
    else:
        num = int(num)
        sides = int(sides)
        rolls = list()
        for each in range(num):
            rolls.append(random.randint(1, sides))
        return rolls


def dice_string(num, sides=6):
    '''Creates a string of dice rolls useful for dicewords'''
    rolls = ''
    for each in range(num):
        if (each != 0 and each % 5 == 0):
            rolls += ':'
        rolls += str(random.randint(1, sides))
    return rolls

def dice_reroll(num, sides=6, reroll=[1], times=0, show_times=True):
    '''
    Rerolls dice that are in reroll amount of times.
    Times = 0 means reroll til value is not in reroll
    '''
    try:
        if isinstance(reroll, int):
            reroll = [reroll]
        elif not isinstance(reroll, list):
            msg ='Invalid value for reroll'
            raise(ValueError)
        elif list(range(1, sides+1)) == reroll:
            msg = 'Reroll values cannot be same as range of dice sides.'
            raise(ValueError)
    except(ValueError):
        print(msg)
    else:
        roll = dice(num, sides, False)

        if times % 1 != 0 or times < 0:
            print("Invalid value for times")
            quit()
        elif times == 0:
            t=1
            while any(dice in reroll for dice in roll):
                roll = [dice(1,sides,False)[0] if time in reroll else time for time in roll]
                t += 1
            if show_times:
                if t == 1:
                    print('Dice were rolled once.')
                else:
                    print(f'Dice were rolled {t} times.')
        else:
            for time in range(1,times+1):
                roll = [dice(1,sides,False)[0] if time in reroll else time for time in roll]
        return roll



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""
    This script rolls a number of variable sided dice.
    """)
    parser.add_argument("number", nargs='?', help="Number of dice", default=2, type=float)
    parser.add_argument("--sides", help="Amount of sides of dice", default=6, type=float)

    args = parser.parse_args()

    number = args.number
    sides = args.sides

    result=dice(number, sides)
    print(result)
