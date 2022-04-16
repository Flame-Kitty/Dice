import random

die = ["1", "2", "3", "4", "5", 6]
toss = random.choice(die)

selection = input("Choose a number from 1 to 6: ")

if selection == toss:
    print("You win! The die landed on " + toss)
else:
    print("You lose! The die landed on " + toss)
