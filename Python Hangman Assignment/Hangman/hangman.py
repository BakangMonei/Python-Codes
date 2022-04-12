import string
import random


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
    guessed = []
    for i in range(len(secret_word)):
        if secret_word[i] in letters_guessed:
            guessed.append(secret_word[i])
        else:
            guessed.append('_ ')
    return ''.join(guessed)


def get_available_letters(letters_guessed):
    lowercase = string.ascii_lowercase
    a = []
    for char in lowercase:
        if char not in letters_guessed:
            a.append(char)
    return ''.join(a)


def hangman(secret_word):
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is %d letters long.' % (len(secret_word)))
    print('You have 3 warnings left.')
    letters_guessed = []
    num_warnings = 0
    i = 0
    while i < 6:
        print('-------------')
        print('You have %d guesses left.' % (6 - i))
        print('Available letters: ', get_available_letters(letters_guessed))
        new_guess = input(str('Please guess a letter: '))
        if str.isalpha(new_guess):
            if str.isupper(new_guess):
                new_guess = str.lower(new_guess)
            if new_guess in letters_guessed:
                num_warnings += 1
                if num_warnings < 4:
                    print('Oops! You\'ve already guessed that letter.You now have %d warnings left:  %s' \
                          % ((3 - num_warnings), get_guessed_word(secret_word, letters_guessed)))
                    # i += 1
                elif num_warnings == 4:
                    print('Oops! You\'ve already guessed that letter.You now have no warnings left: \n '
                          'so you lose one guess:  %s' % (get_guessed_word(secret_word, letters_guessed)))
                    i += 1
                else:
                    break
            else:
                letters_guessed.append(new_guess)
                if is_word_guessed(new_guess, secret_word):
                    print('Good guess:', get_guessed_word(secret_word, letters_guessed))
                    if get_guessed_word(secret_word, letters_guessed) == secret_word:
                        print('------------\nCongratulations, you won!\n'
                              'Your total score for this game is:  %d' % (len(set(secret_word)) * (6 - i)))
                        break
                else:
                    if new_guess in ['a', 'e', 'i', 'o', 'u']:
                        print('Oops! That letter is not in my word: ', \
                              get_guessed_word(secret_word, letters_guessed))
                        i += 2
                    else:
                        print('Oops! That letter is not in my word:\n'
                              'Please guess a letter:', \
                              get_guessed_word(secret_word, letters_guessed))
                        i += 1
        else:
            num_warnings += 1
            if num_warnings < 3:
                print('Oops! That is not a valid letter. You have %d warnings left:  %s' \
                      % ((3 - num_warnings), get_guessed_word(secret_word, letters_guessed)))
                # i += 1
            else:
                break
    if i == 6:
        print('-----------\n'
              'Sorry, you ran out of guesses.'
              ' The word was %s.' % secret_word)


def match_with_gaps(my_word, other_word):
    num = 0
    my_word = my_word.replace(' ', '')
    if len(my_word) == len(other_word):
        for i in range(len(my_word)):
            if my_word[i] == '_' or my_word[i] == other_word[i]:
                pass
            else:
                num += 1
        if num == 0:
            return True
        else:
            return False
    else:
        return False


def show_possible_matches(my_word):
    list = []
    for word in wordlist:
        if match_with_gaps(my_word, word):
            list.append(word)
    if len(list) != 0:
        print(' '.join(list))
    else:
        print('No matches found')


def hangman_with_hints(secret_word):
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is %d letters long.' % (len(secret_word)))
    print('You have 3 warnings left.')
    letters_guessed = []
    num_warnings = 0
    i = 0
    while i < 6:
        # print('You have %d warnings left.' % num_warnings)
        print('-------------')
        print('You have %d guesses left.' % (6 - i))
        print('Available letters: ', get_available_letters(letters_guessed))
        new_guess = input(str('Please guess a letter: '))
        # print(new_guess) #a
        if str.isalpha(new_guess):
            if str.isupper(new_guess):
                new_guess = str.lower(new_guess)
            if new_guess in letters_guessed:
                num_warnings += 1
                if num_warnings < 4:
                    print('Oops! You\'ve already guessed that letter.You now have %d warnings left: %s' \
                          % ((3 - num_warnings), get_guessed_word(secret_word, letters_guessed)))
                elif num_warnings == 4:
                    print('Oops! You\'ve already guessed that letter.You now have no warnings left: \n '
                          'so you lose one guess: %s' % (get_guessed_word(secret_word, letters_guessed)))
                    i += 1
                else:
                    break
            else:
                letters_guessed.append(new_guess)
                if is_word_guessed(new_guess, secret_word):
                    print('Good guess:', get_guessed_word(secret_word, letters_guessed))
                    if get_guessed_word(secret_word, letters_guessed) == secret_word:
                        print('------------\nCongratulations, you won!\n'
                              'Your total score for this game is: %d' % (len(set(secret_word)) * (6 - i)))
                        break
                else:
                    if new_guess in ['a', 'e', 'i', 'o', 'u']:
                        print('Oops! That letter is not in my word:', \
                              get_guessed_word(secret_word, letters_guessed))
                        i += 2
                    else:
                        print('Oops! That letter is not in my word:\n'
                              'Please guess a letter:', \
                              get_guessed_word(secret_word, letters_guessed))
                        i += 1
        elif new_guess == '*':
            show_possible_matches(get_guessed_word(secret_word, letters_guessed))
        else:
            num_warnings += 1
            if num_warnings < 3:
                print('Oops! That is not a valid letter. You have %d warnings left: %s' \
 % ((3 - num_warnings), get_guessed_word(secret_word, letters_guessed)))
                # i += 1
            else:
                break
    if i == 6:
        print('-----------\n'
              'Sorry, you ran out of guesses.'
              ' The word was %s.' % secret_word)


if __name__ == "__main__":
    pass
    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    # secret_word = choose_word(wordlist)
    # hangman(secret_word)
    ###############
    # To test part 3 re-comment out the above lines and
    # uncomment the following two lines.
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)