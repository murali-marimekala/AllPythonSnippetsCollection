#Title : Guess the word with limited attempts

import random
words = ["atlanta", "newyork", "norcross", "johnscreeek", "power", "wisdom", "knowledge"]
secret_Word = random.choice(words)
attempts = 5

print("Guess the word !!")

while attempts > 0:
    guess = input("Enter your guess: ")
    attempts -= 1

    if guess.lower() == secret_Word:
        print("Congratulation you gussed the word correctly")
        break

    else:
        print("Wrong guess. Attempts remaining: ", attempts)

if attempts == 0:
    print("Game over ! The word was", secret_Word)