import random

min_val = 1
max_val = 6

roll_again = "yes"
stop_the_roll = "no"

while roll_again == "yes" or roll_again == "y":
    print("Rolling The Dice...")
    print("The Values are :")

    print(random.randint(min_val, max_val))
    
    roll_again = input("Wanna Roll the Dice Again?")

while stop_the_roll == "no" or stop_the_roll =="n":
    print("Stopping the dice..")