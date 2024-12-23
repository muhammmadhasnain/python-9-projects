# Project 3: Guess the Number Game Python Project (user)

import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    
    while feedback != "c":
        if low != high:
            guess = random.randint(low , high)
        else:
            guess = low

        feedback = input(f"Is {guess} too high (H), too Low (L), or correct (C): ").lower()

        if feedback == "h":
            high = guess - 1
        if feedback == "l":
            high = guess + 1
            
        
    print(f"Yay! The computer guessed your number, {guess}, correctly!")


computer_guess(10)