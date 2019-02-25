import re
import random

    #opens file and reads data, setting as readFile to iterate thru below for cleaning
readFile = open("words.txt")

    #lower cases and inputs to final_word_list
final_word_list = []
for words in readFile:
    final_word_list.append(words.casefold().strip())

    #Breaking final_word_list into lists for the different difficulties
easy_words = []
med_words = []
hard_words = []
for words in final_word_list:
    if len(words) >= 8:
        hard_words.append(words)
    elif len(words) <= 8 and len(words) >= 6:
        med_words.append(words)
    elif len(words) <= 6:
        easy_words.append(words)
  
def set_user_word():
    """User inputs desired difficulty and this returns the appropriate mystery word"""
    user_difficulty = input("Please choose your difficulty (easy, medium, or hard). ")
    if user_difficulty.casefold().strip() == "easy":
        return random.choice(easy_words)
    elif user_difficulty.casefold().strip() == "medium":
        return random.choice(med_words)
    elif user_difficulty.casefold().strip() == "hard":
        return random.choice(hard_words)
    else:
        print("Plese try again, selecting only from (easy, medium, hard). ")
        return set_user_word()

def guess_check():
    """Checks user input value to ensure it's a single character and a letter, reloops until appropriate value provided."""
    guess = input("Please select a letter. ").casefold()
    if not guess.isalpha() or len(guess.strip()) != 1:
        print("Enter only a single letter.")
        return guess_check()
    else:
        return guess

def play_game_again():
    """Asks user if they'd like to play again, tried some error handling with else statement"""
    play_again = input("Would you like to play again (y/n): ")
    if play_again.casefold().strip() == "y":
        game_time()
    elif play_again.casefold().strip() == "n":
        print("Thanks for playing!")
    else:
        print("Please select y or n as your answer. ")
        play_game_again()

def game_time():
    """GAME TIME, this function takes our mystery_word and compiles the guesses 
    and cross checks to see if correct or not, displays progress and keeps counts 
    of attempts."""

    guessed = []
    attempts = 8
    mystery_word = set_user_word()
    
    # print(mystery_word) #testing

    while attempts > 0:

        display = [letter if letter in guessed else "_" for letter in mystery_word]

        print("Guess the word:", (" ".join(display)))

        if "_" not in display: #breaks the while loop once user guesses the word
            break

        print(attempts, "chances left")

        guess = guess_check() #should this funtion take guess as the argument? It's not defined outside the function

        if guess in guessed:
            print("Already guessed", guess)
        elif guess in mystery_word:
            print("Yay")
            guessed.append(guess)
        else:
            print("Nope")
            attempts -= 1
            guessed.append(guess)

    if attempts > 0: # redundant could make a function
        print("You guessed", mystery_word)
    else:
        print("You didn't get", mystery_word)

    play_game_again()

if __name__ == "__main__":
    game_time()

