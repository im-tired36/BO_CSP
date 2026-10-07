#BO, 6th, hangman
import random

words = []
with open("listofwords_hangman.txt", "r") as file:
    wordlist = file.read()
    words = wordlist.split(",")

try:
    with open("winlose_hangman.txt", "r") as win_lose:
        content = win_lose.read()
        counts = content.split(",")
        wins = int(counts[0])
        losses = int(counts[1])

except FileNotFoundError:
    wins = 0
    losses = 0


def display_hangman(wrong_guesses):
    if wrong_guesses == 0:
        print("""
        _____
        |   |
        |
        |
        |
        |_____
        """)

    elif wrong_guesses == 1:
        print("""
        _____
        |   |
        |   O
        |
        |
        |_____
        """)

    elif wrong_guesses == 2:
        print("""
        _____
        |   |
        |   O
        |   |
        |
        |_____
        """)

    elif wrong_guesses == 3:
        print("""
        _____
        |   |
        |   O
        |  /|
        |
        |_____
        """)

    elif wrong_guesses == 4:
        print("""
        _____
        |   |
        |   O
        |  /|\\
        |
        |_____
        """)

    elif wrong_guesses == 5:
        print("""
        _____
        |   |
        |   O
        |  /|\\
        |  /
        |_____
        """)

    elif wrong_guesses == 6:
        print("""
        _____
        |   |
        |   O
        |  /|\\
        |  / \\
        |_____
        """)


def display(word, letters):
    display_word = ""

    for letter in word:
        if letter in letters:
            display_word += letter
        else:
            display_word += "_"

    return display_word

while True:
    correct_word = random.choice(words).strip().lower()
    wrong_guesses = 0
    letters_guessed = []

    print("Loading words from listofwords_hangman.txt")
    print(f"Loading stats from winlose_hangman.txt (wins:{wins}, losses:{losses})")

    while True:

        display_hangman(wrong_guesses)
            
        print("this is the word:", display(correct_word, letters_guessed))
        if len(letters_guessed) == 0:
            print("You haven't guessed any letters yet.wrong_guesses")
        else:
            print(f"You've guessed these letters: {letters_guessed}")
        
        print(f"You've made {wrong_guesses} wrong guesses out of 6")

        guess = input("Guess a letter: ").lower()

    
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter.")
            continue

        if guess in letters_guessed:
            print("You already guessed that letter!")
            continue

        letters_guessed.append(guess)
        
        if guess not in correct_word:
            wrong_guesses += 1
            print("That letter isn't in the word.")
        
        if display(correct_word, letters_guessed) == correct_word:
            print(f"Yay! You guessed the word: {correct_word}")
            wins += 1
            break

        if wrong_guesses == 6:
            display_hangman(wrong_guesses)
            print("\nYou ran out of guesses and lost.")
            print("The word was:", correct_word)
            losses += 1
            break

    with open("winlose_hangman.txt", "w") as win_lose:
        win_lose.write(str(wins) + "," + str(losses))

    print("\nAll-time stats:")
    print(f"Number of wins: {wins}")
    print(f"Number of losses: {losses}")

    play_again = input("\nWould you like to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break

        