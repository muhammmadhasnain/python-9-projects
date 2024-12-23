# Project 2: Guess the Number Game Python Project (computer)

import random


def guess(x):
    random_num = random.randint(1, x)
    guess = 0
    while random_num != guess:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess < random_num:
            print("Sorry, guess again. Too Low. ")
        elif guess > random_num:
            print("Sorry, guess again. Too High. ")
        
    print(f"Yay, congrats. You have guessed the number {random_num}")


guess(10)