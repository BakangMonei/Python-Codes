# Problem Set 2, hangman.py
# Name: Melissa Tshipietsile
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def choose_word(wordlist):
    return random.choice(wordlist)


wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    for char in secret_word:
        if char not in letters_guessed:
            return False
        else:
            return True


def get_guessed_word(secret_word, letters_guessed):
    guessed_word = ''
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word += '_'
    return guessed_word


def get_available_letters(letters_guessed):
    availableLetters = ''
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            availableLetters += letter
    return availableLetters


def hangman(secret_word):
    warnings_left = 3
    guesses_left = 0
    letters_guessed = []

    print("Welcome to the game hangman!")
    print("I am thinking of a word that is{0}".format(str(len(secret_word)) + "letters long"))
    print("You have" + str(warnings_left) + "warnings left.")
    print("------------------")

    while True:
        print("You have " + str(6 - guesses_left) + " guesses left.")

        availableLetters = get_available_letters(letters_guessed)

        print("Available letters: " + availableLetters)

        guess_letter = input("Please guess a letter: ").lower()

        if guess_letter not in string.ascii_lowercase:
            warnings_left -= 1
            print("Please enter valid English alphabet to guess the word." + "You have{} warning left: ".format(
                warnings_left), get_guessed_word(secret_word, letters_guessed))
            print("------------")
            continue
        if guess_letter not in letters_guessed:
            letters_guessed.append(guess_letter)
            if guess_letter in secret_word:
                print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_left += 1
                print("Oops! That letter is not in my word: ", get_guessed_word(secret_word, letters_guessed))

        else:
            print("Oops! You've already guessed that letter: " + "You have{} warnings left: ".format(warnings_left),
                  get_guessed_word(secret_word, letters_guessed))
        print("------------")

        if secret_word == get_guessed_word(secret_word, letters_guessed):
            print("congratulations, you won")
            break
        elif guesses_left == 6:
            print("Sorry, you ran out of guesses. The word was " + secret_word + ".")
            break


def match_with_gaps(my_word, other_word):
    if len(my_word) != len(other_word):
        return False
    for i in range(len(my_word)):
        if my_word[i] != "_" and my_word[i] != other_word[i]:
            return False
    return True


def show_possible_matches(my_word):
    match_found = False
    for word in wordlist:
        if match_with_gaps(my_word, word):
            print(word, end=" ")
            match_found = True
    if match_found:
        print()


def hangman_with_hints(secret_word):
    warnings_left = 3
    guesses_left = 0
    letters_guessed = []

    print("Welcome to the game hangman!")
    print("I am thinking of a word that is{}".format(str(len(secret_word)) + "letters long"))
    print("You have" + str(warnings_left) + "warnings left.")
    print("------------------")

    while True:
        print("You have " + str(6 - guesses_left) + " guesses left.")

        availableLetters = get_available_letters(letters_guessed)

        print("Available letters: " + availableLetters)

        guess_letter = input("Please guess a letter: ").lower()

        if guess_letter not in string.ascii_lowercase:
            warnings_left -= 1
            print("Please enter valid English alphabet to guess the word." + "You have{} warning left: ".format(
                warnings_left), get_guessed_word(secret_word, letters_guessed))
            print("------------")
            continue
        if guess_letter not in letters_guessed:
            letters_guessed.append(guess_letter)
            if guess_letter in secret_word:
                print("Good guess: ", get_guessed_word(secret_word, letters_guessed))
            else:
                guesses_left += 1
                print("Oops! That letter is not in my word: " + "You have{} warnings left: ".format(warnings_left),
                      get_guessed_word(secret_word, letters_guessed))

        else:
            print("Oops! You've already guessed that letter: " + "You have{} warning left: ".format(warnings_left),
                  get_guessed_word(secret_word, letters_guessed))
        print("------------")

        if secret_word == get_guessed_word(secret_word, letters_guessed):
            print("congratulations, you won")
            break
        elif guesses_left == 6:

            print("Sorry, you ran out of guesses. The word was " + secret_word + ".")
            break


if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    secret_word = choose_word(wordlist)
    hangman(secret_word)

    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.

    # secret_word = choose_word(wordlist)
    # hangman_with_hints(secret_word)
