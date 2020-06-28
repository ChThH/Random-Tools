import random
import argparse


def dice(num, var=6):
    '''Rolls a num(ber) of var(ible) sided dice'''
    if num % 1 != 0:
        print('I\'m not rolling a fractional die for anyone.')
        quit()
    if var % 1 != 0:
        print('Seriously, I can\'t roll dice with fractional sides; what would that even mean?')
        quit()
    if num == 0:
        print('So you don\'t want to roll any dice.')
        quit()
    if num < 0:
        print('Negative numbers, huh? \nOkay, you roll the dice then. Let me know how it goes.')
        quit()
    if var < 1:
        print ("I see you're unfamiliar with dice. Dice must have at least one side.")
        quit()

    if num == 1 and var == 1:
        print('What\'s the point of rolling a 1-sided die?')
    elif num == 1 and var == 2:
        print('So you\'re flipping a coin.')
    elif var == 1:
        print("What's the point of rolling 1-sided dice?")
    elif var == 2:
        print('Let the coin flipping begin!')

    num = int(num)
    var = int(var)

    rolls = list()
    for each in range(num):
        # print(each)
        rolls.append(random.randint(1, var))
    return rolls


def dice_string(num, var=6):
    '''Creates a string of dice rolls useful for dicewords'''
    rolls = ''
    for each in range(num):
        if (each != 0 and each % 5 == 0):
            rolls += ':'
        rolls += str(random.randint(1, var))
    return rolls


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""
    This script rolls a number of variable sided dice. 
    """)
    parser.add_argument("number", help="Number of dice", type=float)
    parser.add_argument("--sides", help="Amount of sides of dice", default=6, type=float)

    args = parser.parse_args()

    number = args.number
    sides = args.sides

    result=dice(number, sides)
    print(result)