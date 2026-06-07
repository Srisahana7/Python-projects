# Project: Stone Paper Scissors Game
# Author: Sri Sahana
# Concepts Used:
# - Lists
# - Loops
# - User Input
# - Conditional Statements
# - Random Module
# Description:
# A simple Stone-Paper-Scissors game where the user plays
# against the computer for multiple rounds.
import random
computer_choice=["stone","paper","scissor"]
print("Let's play")
print("Choose one of the following")
print("YOUR CHOICES: Stone , Paper , Scissor ")
n=int(input("How many do you want to play= "))
for i in range(n):
    pick=random.choice(computer_choice)
    user_choice=input("Select your choice= ").lower()
    if user_choice not in computer_choice:
        print("Invalid choice")
        continue
    elif user_choice == pick:
        print("My choice is also" , pick ,"\nMatch draw")
    else:
        if user_choice == "paper" and pick == "scissor":
            print("Wow! My choice is ", pick,"\nI won the match")
        elif user_choice == "scissor" and pick == "paper":
            print("Wow! My choice is ", pick,"\nYou won the match")
        elif user_choice == "stone" and pick == "paper":
            print("Wow! My choice is ", pick,"\nI won the match")
        elif user_choice == "paper" and pick == "stone":
            print("Wow! My choice is ", pick,"\nYou won the match")
        elif user_choice == "scissor" and pick == "stone":
            print("Wow! My choice is ", pick,"\nI won the match")
        else:
            print("Wow! My choice is ", pick,"\nYou won the match")
print("Thank you for playing!!!!!")    
    
    
