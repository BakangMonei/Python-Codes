# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string
import os
import numpy

WORDLIST_FILENAME = "words.txt"


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print
    "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    for i in range(len(secretWord)):
        if secretWord[i] not in lettersGuessed:
            return False
    else:
        return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    word = '_' * len(secretWord)
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            word = word[:i] + secretWord[i] + word[i + 1:]
    return word


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    import string
    avl = list(string.ascii_lowercase)
    for i in range(len(lettersGuessed)):
        if lettersGuessed[i] in avl:
            avl.remove(lettersGuessed[i])
    return ''.join(avl)


def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print
    "Welcome to the game, Hangman!"
    print
    "I am thinking of a word that is " + str(len(secretWord)) + " letters long"
    print("-------------")
    turns = 8
    mistakesMade = ''
    lettersGuessed = []
    "\n"
    wordIsGuessed = False
    avl = list(getAvailableLetters(lettersGuessed))
    gamedone1 = False
    gamedone2 = False

    while True:
        getGuessedWord(secretWord, lettersGuessed)
        print('You have ' + str(turns) + ' guesses left')
        print('Available letters: ' + str(getAvailableLetters(lettersGuessed)))
        guess = input('Type guess a letter: ')
        guess = guess.lower()
        if guess in getAvailableLetters(lettersGuessed):
            turns = turns - 1
        else:
            turns = turns
        lettersGuessed = lettersGuessed + list(guess)
        # if isWordGuessed(secretWord,lettersGuessed)==False:
        if guess in secretWord:
            print('Good guess: ' + str(getGuessedWord(secretWord, lettersGuessed)))
            print("-------------")
            if isWordGuessed(secretWord, lettersGuessed) == True:
                gamedone1 = True
        elif guess not in secretWord and turns != 0:
            print('Oops! That letter is not in my word: ' + str(getGuessedWord(secretWord, lettersGuessed)))
            print('-------------')

            ##            avl1=avl-avl[guess]
            ##            if guess not in list(avl1):
            ##                turns = turns-1
            if turns == 0:
                gamedone2 = True
        if gamedone1:
            print('Congratulations, you won!')
            break
        if gamedone2:
            print("Sorry, you ran out of guesses. The word was " + str(secretWord))
            break

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)