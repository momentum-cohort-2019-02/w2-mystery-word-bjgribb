import re
import random

    #opens file and reads data, setting as readFile to iterate thru below for cleaning
readFile = open("words.txt", 'r')

    #lower cases and inputs to word_list
word_list = []

for words in readFile:
    word_list.append(words.casefold())

    #strips whitespace and inputs to final_word_list
final_word_list = []

for words in word_list:
    final_word_list.append(words.strip())

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
  
    #Now I want to work on getting the function to take user input on difficulty and randomly generate word appropriate list


def set_user_word():
    """User inputs desired difficulty and this returns the appropriate mystery word"""
    user_difficulty = input("Please choose your difficulty (easy, medium, or hard). ")
    if user_difficulty.casefold() == "easy":
        mystery_word = random.choice(easy_words)
        return mystery_word
    elif user_difficulty.casefold() == "medium":
        mystery_word = random.choice(med_words)
        return mystery_word
    elif user_difficulty.casefold() == "hard":
        mystery_word = random.choice(hard_words)
        return mystery_word
    else:
        print("Plese try again, selecting only from (easy, medium, hard). ")
        return set_user_word()

def guess_check():
    """Checks user input value to ensure it's a single character and a letter, reloops until appropriate value provided."""
    guess = input("Please select a letter. ")
    if not guess.isalpha():
        print("Enter only letters.")
        return guess_check()
    if len(guess) != 1:
        print("Enter only a single letter.")
        return guess_check()
    else:
        return guess

def play_game_again():
    """Asks user if they'd like to play again, tried some error handling with else statement"""
    play_again = input("Would you like to play again (y/n): ")
    if play_again.casefold() == "y":
        game_time()
    elif play_again.casefold() == "n":
        print("Thanks for playing!")
    else:
        print("Please select y or n as your answer. ")
        play_game_again()

def game_time():
    """GAME TIME, this function takes our mystery_word and compiles the guesses 
    and cross checks to see if correct or not, displays progress and keeps counts 
    of attempts. Should try and break up a bit."""

    guessed = []
    attempts = 8
    mystery_word = set_user_word()
    
    # print(mystery_word) #testing

    while attempts > 0:

        """uh-oh! this keeps running even if the player guesses the word (makes 
        sense since it's only accounting for attempts need to incorporate check 
        for letter if letter in guessed if in mystery_word?)"""

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

    if attempts > 0: 
        print("You guessed", mystery_word)
    else:
        print("You didn't get", mystery_word)

    play_game_again()

game_time()



