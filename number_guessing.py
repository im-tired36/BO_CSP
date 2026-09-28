#BO, 6th, number guessing game
import random



for number in range(1,6):
    guess = input("Guess a number: ") 
    if guess == number:
        print("Correct")
    elif guess > number:
        print("Too High! Try again")
    elif guess < number:
        print("Too low! Try again")
