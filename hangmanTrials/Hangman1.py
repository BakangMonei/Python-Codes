import random
import string

WORDLIST_FILENAME = 'words.txt'
def loadWordList():
 print('Loading word list from file…')
 inFile = open(WORDLIST_FILENAME, 'r', 0)
 line = inFile.readline()
 wordlist = string.split(line)
 print(' ', len(wordlist), 'words loaded.')
 return wordlist
def chooseRandomWord(wordlist):
 return random.choice(wordlist)
# end of helper code
# — — — — — — — — — — — — — — — — — -