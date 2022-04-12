# Problem Set 2, hangman.py
# Name: 
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
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    for i in secret_word:
        if i not in letters_guessed:
            return False
        else:
            return True
#secret_word = 'apple'
#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(is_word_guessed(secret_word, letters_guessed))


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    userguess = ' '
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            userguess += secret_word[i]
        else:
            userguess += '_ '
    return userguess

#secret_word = 'apple'
#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
#print(get_guessed_word(secret_word, letters_guessed))


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    availletters = ' '
    alphabets = string.ascii_lowercase
    for letter in alphabets:
        if letter not in letters_guessed:
            availletters += letter
    return availletters.lower()
#letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
#print (get_available_letters(letters_guessed))

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    print('Welcome to the game Hangman!')
    lensecretWord = choose_word((wordlist))
    print('I am thinking of a word that is %s letters long.'% (len(lensecretWord)))
    print('You have 3 warnings left.')
    letters_guessed = []
    num_of_warnings = 0
    x = 0
    dashes = '--------'
    while x < 6:
        print(dashes)
        print('You have %d guesses left.' % (6 - x))
        print('Available letters:' , get_available_letters(letters_guessed))
        user_guess =input(str('Please guess a letter: '))
        if str.isalpha(user_guess): #checking if user input is an alphabet and making it lower caps
            if str.isupper(user_guess):
                user_guess = str.lower(user_guess)
            if user_guess in letters_guessed:
                num_of_warnings += 1
                if num_of_warnings < 4:
                    print("Oops! You've already guessed that letter. You have %d warnings left: %s" % ((3 - num_of_warnings), get_guessed_word(secret_word,letters_guessed)))
                elif num_of_warnings == 4:
                    print("Oops! You've already guessed that letter. You have 0 warnings left: %s" % (get_guessed_word(secret_word,letters_guessed)))
                    x += 1
                else:
                    break
            else: #game termination for a winning
                letters_guessed.append(user_guess)
                if is_word_guessed(user_guess, secret_word):
                    print('Good guess:', get_guessed_word(secret_word, letters_guessed))
                    if get_guessed_word(secret_word, letters_guessed) == secret_word:
                        set_secretword = set(secret_word)
                        print(dashes)
                        print('Congratulations, you won! \n Your total score for this game is: %d' % (len(set_secretword) * (6 - x)))
                        break
                else: #Game rules for : vowels , cosonants
                    vowels = ['a', 'e', 'i', 'o', 'u']
                    if user_guess in vowels:
                        print('Oops! That letter is not in my word: %s' % (
                            get_guessed_word(secret_word, letters_guessed)))
                        x += 2
                    else:
                        print('Oops! That letter is not in my word: %s' % (
                            get_guessed_word(secret_word, letters_guessed)))
                        x += 1

        else: #deducting from warnings when user inputs symbols/numbers or entering an already entered letter
            num_of_warnings += 1
            if num_of_warnings < 3:
                print('Oops! That is not a valid letter. You have %d warnings left: %s' % ((3 - num_of_warnings), get_guessed_word(secret_word, letters_guessed)))

            else: #deducting from guesses after warning finish
                print("Oops! You've already guessed that letter. You have 0 warnings left: %s" % (get_guessed_word(secret_word, letters_guessed)))
                x+= 1
    if x == 6: #game termination for losing
        print(dashes)
        print('Sorry, you ran out of guesses. \n The word was %s.' % (secret_word))













# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    number = 0
    my_word = my_word.strip()
    if len(my_word) == len(other_word):
        for i in range(len(my_word)):
            if my_word[i] == other_word[i] or my_word[i] == '_':
                pass
            else:
                number += 1
        if number == 0:
            return True
        else:
            return False
    else:
        return False

#match_with_gaps("te_ t", "tact")
#match_with_gaps("a_ _ le", "banana")
#match_with_gaps("a_ _ le", "apple")

def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    lst = []
    for i in wordlist:
        if match_with_gaps(my_word, i):
            lst.append(i)

    if len(lst) != 0:
        print(' '.join(lst))
    else:
        print('No matches found')
#print(show_possible_matches("t_ _ t"))
#tact tart taut teat tent test text that tilt tint toot tort tout trot tuft
#twit
#print(show_possible_matches("abbbb_ "))
#No matches found
#print(show_possible_matches("a_ pl_ "))
#ample amply


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"

    print('Welcome to the game Hangman!')
    lensecretWord = choose_word((wordlist))
    print('I am thinking of a word that is %s letters long.' % (len(lensecretWord)))
    print('You have 3 warnings left.')
    letters_guessed = []
    num_of_warnings = 0
    x = 0
    dashes = '--------'
    while x < 6:
        print(dashes)
        print('You have %d guesses left.' % (6 - x))
        print('Available letters:', get_available_letters(letters_guessed))
        user_guess = input(str('Please guess a letter: '))
        if str.isalpha(user_guess):  # checking if user input is an alphabet and making it lower caps
            if str.isupper(user_guess):
                user_guess = str.lower(user_guess)
            if user_guess in letters_guessed:
                num_of_warnings += 1
                if num_of_warnings < 4:
                    print("Oops! You've already guessed that letter. You have %d warnings left: %s" % (
                    (3 - num_of_warnings), get_guessed_word(secret_word, letters_guessed)))
                elif num_of_warnings == 4:
                    print("Oops! You've already guessed that letter. You have 0 warnings left: %s" % (
                        get_guessed_word(secret_word, letters_guessed)))
                    x += 1
                else:
                    break
            else:  # game termination for a winning
                letters_guessed.append(user_guess)
                if is_word_guessed(user_guess, secret_word):
                    print('Good guess:', get_guessed_word(secret_word, letters_guessed))
                    if get_guessed_word(secret_word, letters_guessed) == secret_word:
                        set_secretword = set(secret_word)
                        print(dashes)
                        print('Congratulations, you won! \n Your total score for this game is: %d' % (
                                    len(set_secretword) * (6 - x)))
                        break
                else:  # Game rules for : vowels , consonants
                    vowels = ['a', 'e', 'i', 'o', 'u']
                    if user_guess in vowels:
                        print('Oops! That letter is not in my word: %s' % (
                            get_guessed_word(secret_word, letters_guessed)))
                        x += 2
                    else:
                        print('Oops! That letter is not in my word: %s' % (
                            get_guessed_word(secret_word, letters_guessed)))
                        x += 1

        elif user_guess == '*': #asterisk used to print out hints for the user
         show_possible_matches(get_guessed_word(secret_word,letters_guessed))

        else:  # deducting from warnings when user inputs symbols/numbers or entering an already entered letter
            num_of_warnings += 1
            if num_of_warnings < 3:
                print('Oops! That is not a valid letter. You have %d warnings left: %s' % (
                (3 - num_of_warnings), get_guessed_word(secret_word, letters_guessed)))

            else:  # deducting from guesses after warning finish
                print("Oops! You've already guessed that letter. You have 0 warnings left: %s" % (
                    get_guessed_word(secret_word, letters_guessed)))
                x += 1

    if x == 6:  # game termination for losing
        print(dashes)
        print('Sorry, you ran out of guesses. \n The word was %s.' % (secret_word))




# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
