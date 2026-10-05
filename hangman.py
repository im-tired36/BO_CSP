#BO, 6th, hangman
import random

#create a list of 10 words on a seperate txt file
words = []
with open("listofwords_hangman.txt", "r") as list:
    wordlist = list.read()
    words = wordlist.split(",")
#use split( ",") on th econtent of the words txt document to create your list of words

#create another file that only holds win/lose counts
win_lose_counts = []
with open("winlose_hangman.py", "r") as win_lose:
    content = win_lose.read()    
#pull win and lose totals from the other txt file and save then as 2 seperate variables


#build hangman game
#save the correct word as a variable random.choice(name of list)
#keep track of number of wrong guesses
#what letters have been guessed
correct_word = random.choice(words)
right_guess = content[0]
wrong_guess = content[0]
letters_guessed = 

#function to display the hangman (need number of wrong guesses)
"""_____
   |    |
   |    O
   |   /|\\
   |   / \\
   |______ 
"""
   
#function to show the letters and spaces (the correct word, letters that have been guessed)
def display(hangman, word, letters):
    
#loop over the correct word
   #variable for display word the _ _ _ (starts as an empty string) 
   #check if letter has been guessed
      #then add the letter to the display word
   #if they haven't guessed the letter
      #add an underscore to the display word
#return the finished display word (outside the loop)

#main game loop (while true)
#call the function to show hangman
#print function call to show display word
#create a variable and ask the user to guess a letter
#add the letter to our guess letters list
#check if the letter is not the word
   #increase incorrect guesses
#check if the display word is the same as the word
   #tell the user they won
   #ask if they wont to play again
      #reset random word, wrong guess count, 
#check to see if the user lost (if they have 6 wrong guesses)
   #tell them they lost
   #tell them what the word was
   #increase the lost count
   #ask if they want to play again
                   #reset random word and wrong guess count