
# Project 5: Hangman Python Project

import random

words = ['python', 'java', 'code', 'game', 'hangman']
word = random.choice(words)
guessed = ["_"] * len(word)
attemps = 6 

print("welcome to Hangman!")
print(' '.join(guessed))

while attemps > 0 and "_" in guessed:
    guess = input("\nGuess a letter: ").lower()
    if guess in word:
        for i , letter in enumerate(word):
            if letter == guess:
                guessed[i] = letter
        print("correct")
    else:
        attemps -= 1
        print(f"wrong you have {attemps} attemps left.")

    print(' '.join(guessed))


if "_" not in guessed:
    print("\nCongratulations, you guessed the word!")
else:
    print(f"\nGame over! The word was '{word}'.")