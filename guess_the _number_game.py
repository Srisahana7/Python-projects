# Project: Guess the Number Game
# Author: Sri Sahana
# Description:
# The computer generates a random number between 1 and 100.
# The user has 3 attempts to guess the correct number.
# Invalid inputs are rejected and do not count as attempts.

# Concepts Used:
# - Random Module
# - While Loop
# - Conditional Statements
# - User Input
# - Input Validation (isdigit)

import random
# Generate a random number between 1 and 100
num=random.randint(1,100)
print("You have only 3 attempts! Try well.....")
print("Guess the number from 1 to 100!")
# Track the number of attempts
attempt=0
while attempt < 3:
    guess=input("Guess the number= ")
    print("\n")
    # Check if the input contains only digits
    if not guess.isdigit():
        print("You typed an invalid guess" ,guess, "\nType numbers only.")
        continue
    else:
        guess = int(guess)
        attempt+=1
        if guess==num:
            print("Wow! Extraordinary your guess ",guess, "is correct")    
            print("You won at" ,attempt, "attempts")
            break
        # Give hints to the user
        elif guess>num:
            print("Ohh! Your guess" ,guess, "is higher")
        else:
            print("Ohh! Your guess" ,guess, " is lower")
        print("You already played",attempt, "attempts")
# Runs only if the loop finishes without a break
else:
    print("You lost the game!!!")
    print("The correct number is ",num)
               
