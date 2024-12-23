# Project 4: Rock, paper, scissors Python Project

import random

def play():
    user = input("'r' for Rock, 'p' for Paper, 's' for scissors: ")
    computer = random.choice(["r", "p", "s"])

    print(user , computer)
    if user == computer:
        return "tie"
    
    if is_win(user , computer):
        return "You Win!"

    return "You Lose!"

def is_win(player , opponent):
    if(player == "r" and opponent == "s") or (player == "p" and opponent == "r")\
         or (player == "s" and opponent == "p"):
         return True

    


print(play())