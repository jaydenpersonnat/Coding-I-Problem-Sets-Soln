                          # Guess

# Goal: Create a guessing game that contains a loop so that a user can keep playing until they guess correctly!


"""
Your Mission: 
    Create a program that asks the user to guess a randomly generated number 
    from 1 to 100 (random.randint() could come in handy!). If the user guesses 
    too high, too low, or gets it, let the user know with print statements 
    like below! Of course, if the user gets it right, be sure to end the while 
    loop that is making the game continue on!


# Example Run: 
    $ python guess.py
    Guess the number: 17
    Too low!
    Guess the number: 61
    Too high!
    Guess the number: 42
    You got it!

""" 

# Code goes below 
import random

# modules - contain functions that someone has written in the past 
# random module - contains a bunch of functions that are going to help you deal with random elements 

# Calculate number using random module 
number = random.randint(1, 100) 

# Get user input for guess; if guess is too high or low, continue to prompt user until correct 
while True:
    guess = int(input("Guess the number: ")) 

    if guess < number: 
        print("Too low!")
    elif guess > number: 
        print("Too high!")
    else:
        print("You got it")
        break




