import random

target = random.randint(1, 500)

guess = 0
attempts = 0

print("Guess the number between 1 and 500 Rana !!")

while guess != target:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < target:
        print("Too low !! Guess higher Rana !!.")
    elif guess > target:
        print("Too high ! Guess lower Rana !!.")
    else:
        print("Congratulations Rana ! you guessed it.")
        print("Number of attempts you tried are : ", attempts)