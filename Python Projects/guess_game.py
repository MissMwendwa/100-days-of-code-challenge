# Todays project is a guessing game in python.
# It allows the user to guess a numbers and checks the validity

# Imports
import random

# The game

# Inputs
num = random.randint(1, 10)
guess = int(input('Enter a number: '))

# the validity checker
while num != guess:
    if guess < num:
        print(" The number is too Low!")
        guess = int(input('Enter another number: '))
    elif guess > num:
        print(" Number is too High!")
        guess = int(input('Enter another number: '))
    else:
        break

print("Your Guess is Correct!")