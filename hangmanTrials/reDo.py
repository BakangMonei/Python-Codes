import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWordList():
    print("Loading word from file...")
    infile = open("words.txt", "r")
    line = infile.readline()
    wordlist = string.split(line)
    print(" ", len(wordlist), "words loaded")
    return wordlist

def chooseRandomWord(wordlist):
    return random.choice(wordlist)

def checkGuess(guess, secretWord):
    if guess in secretWord:
        return True
    else:
        return False

def getGuessWord(secretWord, lettersGuessed):
    guess = " "
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            guess += secretWord[i]
        else:
            guess += "_ "
    return guess

def getAvailLetters(lettersGuessed):
    lettersAvailable = " "
    for letter in "abcdefghijklmnopqrstuvwxyz":
        if letter not in lettersGuessed:
            lettersAvailable += letter
    return lettersAvailable.lower()

def isGuessed(secretWord, lettersGuessed):
    count = 0
    for letter in lettersGuessed:
        if letter in secretWord:
            count += 1
    if count == len(secretWord):
        return True
    else:
        return False

def hangman(secretWord):
    lettersGuessed = []
    guessCount = 8
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is %d long" % len(secretWord))

    while not(isGuessed(secretWord, lettersGuessed)) and guessCount &amp:
        print("________")
        print("You have %d guesses left" % guessCount)
        print("Available letters: %s" % getAvailLetters(lettersGuessed))
        guess = input("Please guess a letter: ").lower()

        if guess in lettersGuessed:
            print("Oops! Youve already guessed that letter: %s" %getGuessWord(secretWord, lettersGuessed))
        elif guess not in "abcdefghijklmnopqrstuvwxyz":
            print("Oops! That is not a letter: %s" %getGuessWord(secretWord, lettersGuessed))
        elif checkGuess(guess, secretWord):
            lettersGuessed += guess
            print("Good guess: %s" %getGuessWord(secretWord, lettersGuessed))
        else:
            lettersGuessed += guess
            print("Oops! This is not in my word: %s" %getGuessWord(secretWord, lettersGuessed))
            guessCount -= 1
            print("------------")
            if guessCount == 0:
                print("Sorry!! You have run out of guesses. The word was %s." %secretWord)
            else:
                print("Congradulations!! you won")