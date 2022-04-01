import random
import re

def roll_die(num_sides):
    return random.randint(1, num_sides)


while True:
    user_choice = input("ROLL: ")
    print("")
    
    if not re.match(r'[1-9]+[dD][1-9]+', user_choice):
        break

    split_choice = user_choice.split('d')

    number_of_dice = int(split_choice[0])
    sides_per_die = int(split_choice[1])


    rolls = []
    for i in range(number_of_dice):
        roll = roll_die(sides_per_die)
        rolls.append(roll)
        print(f"roll #{i+1}:\n{roll}\n")
    print(f"\nTotal: {sum(rolls)}")
    print(f"Average: {int(sum(rolls)/len(rolls))}")
    print('\n'*2)


