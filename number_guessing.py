#BO, 6th, number guessing game

import random

number = random.randint(1, 100)
attempts = 6
guesses_used = 0

print("Choose a number from 1 to 100 to guess the number I chose.")
print("You have 6 attempts.")

for attempt in range(attempts):
    guess = int(input(f"This is your #{attempt + 1} try: "))
    guesses_used += 1
   
    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"Correct! You guessed it in {guesses_used} tries!")
        break
else:
    print(f"You're out of guesses! The number was {number}.")
