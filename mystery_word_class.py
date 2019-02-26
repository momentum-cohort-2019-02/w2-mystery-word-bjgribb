import random

def set_user_mystery_word():
    """Takes user difficulty selection and returns a random word from the appropriate difficulty list"""
    difficulty = input("Please choose a difficulty (easy, medium, hard): ").casefold().strip()
    if difficulty == "easy":
        return(random.choice(easy_words))
    elif difficulty == "medium":
        return(random.choice(medium_words))
    elif difficulty == "hard":
        return(random.choice(hard_words))
    else:
        set_user_mystery_word()

def guess_check():
    """Checks user input value to ensure it's a single character and a letter, loops until appropriate value provided."""
    guess = input("Please select a letter. ").casefold()
    if not guess.isalpha() or len(guess.strip()) != 1:
        print("Enter only a single letter.")
        return guess_check()
    else:
        return guess

def play_game_again():
    """Asks user if they'd like to play again, loops until appropriate value is provided"""
    play_again = input("Would you like to play again (y/n): ")
    if play_again.casefold().strip() == "y":
        game_time(mystery_word)
    elif play_again.casefold().strip() == "n":
        print("Thanks for playing!")
    else:
        print("Please select y or n as your answer. ")
        play_game_again()

def game_time(mystery_word):
    """GAME TIME, this function takes our mystery_word and compiles the guesses 
    and cross checks to see if correct or not, displays progress and keeps counts 
    of attempts."""

    guessed = []
    attempts = 8
    

    while attempts > 0:

        display = [letter if letter in guessed else "_" for letter in mystery_word]

        print("Guess the word:", (" ".join(display)))

        if "_" not in display: #breaks the while loop once user guesses the word
            break

        print(attempts, "chances left")

        guess = guess_check()

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

if __name__ == "__main__":

    readFile = open("words.txt")
    word_list = [words.casefold().strip() for words in readFile]
    easy_words = [word for word in word_list if len(word) >= 4 and len(word) <= 6]
    medium_words = [word for word in word_list if len(word) >= 6 and len(word) <= 8]
    hard_words = [word for word in word_list if len(word) >= 8]

    mystery_word = set_user_mystery_word()

    game_time(mystery_word)

