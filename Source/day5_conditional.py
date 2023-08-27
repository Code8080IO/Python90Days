"""
@author : code8080.in

How to Use the Program
    Run the program.
    It will prompt you to guess a number between 1 and 100.
    Enter your guess.
    The program will give you a hint ("Too high!" or "Too low!") based on your guess.
    You can continue guessing until you find the correct number or choose to quit.
"""

import random

def guess_the_number():
    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)
    
    print("Welcome to the Guess the Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    attempts = 0
    
    while True:
        # Take user input
        user_guess = int(input("What's your guess? "))
        attempts += 1
        
        # Check the guess using conditional statements
        if user_guess == random_number:
            print(f"Congratulations! You've guessed it right in {attempts} attempts.")
            break
        elif user_guess > random_number:
            print("Too high! Try again.")
        else:
            print("Too low! Try again.")
        
        # Ask if the user wants to continue guessing
        continue_guessing = input("Do you want to continue guessing? (yes/no) ")
        
        if continue_guessing.lower() != 'yes':
            print(f"The correct number was {random_number}. Better luck next time!")
            break

# Run the function to start the game
guess_the_number()
