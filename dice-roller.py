import random
import re

def roll_die(num_sides):
    return random.randint(1, num_sides)

while True:
    user_choice = input("ROLL: ").lower()
    print("")
    
    if not re.match(r'[1-9]+[d][1-9]+', user_choice):
        print('EXITING PROGRAM...')
        print('Valid choices use this syntax: <NUMBER OF DICE>d<SIDES PER DIE>\n\
        Examples: 1d20 (rolls 1 die with 20 sides each); 3d8 (rolls 3 dice with 8 sides each')
        print()
        break

    split_choice = user_choice.split('d')

    number_of_dice = int(split_choice[0])
    sides_per_die = int(split_choice[1])


    rolls = []
    for i in range(number_of_dice):
        roll = roll_die(sides_per_die)
        rolls.append(roll)
        print(f"Roll #{i+1}:\n{roll}\n")
    print("")
    print(f"Total: {sum(rolls)}")
    print(f"Average: {int(sum(rolls)/len(rolls))}")
    print('\n'*2)


