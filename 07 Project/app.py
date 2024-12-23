# Project 7: Password Generator Python Project

import random

char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&().1234567890"

number = int(input("Amount of password generated: "))

length = int(input("length of password: "))

for pwd in range(number):
    password = ""
    for c in range(length):
        password += random.choice(char)
    print(f"Password: {password}")




