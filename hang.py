import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print 'Loading word list from file...'
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def validWorld(guessWord, guesses):
    letter = string.ascii_lowercase
    differentLetters = []
    for letter in guessWord:
        if letter not in differentLetters:
            differentLetters.append(letter)

    if len(differentLetters) > guesses:
        print 'The number of Different Letters it is more than number of Guesses'
        return False

    print 'Number of Different Letters:', len(differentLetters), '.'
    return True

def chooseAWord(wordlist, guesses):
    chosenWord = random.choice(wordlist)
    if validWorld(chosenWord, guesses):
        return chosenWord
    chooseAWord(wordlist, guesses)

def isWordGuessed(secretWord, lettersGuessed):

#    secretLetters = []
#    for letter in secretWord:
#        if letter in secretLetters:
#            secretLetters.append(letter)
#        else:
#            pass

    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
            return False

    return True

def getAvailableLetters():
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase
    return available

def updateAvailableLetter(availableLetters, lettersGuessed):
    for letter in lettersGuessed:
        availableLetters = availableLetters.replace(letter, '')
    return availableLetters

def validLetter(letter, lettersGuessed):
    if letter in lettersGuessed:
        return False
    return True

#def getGuessedWord():
#     guessed = ''
#     return guessed

def printSecretWord(lettersGuessed, secretWord):
    word = ''
    for letter in secretWord:
        if letter in lettersGuessed:
            word += letter
        else:
            word += '_'
        print word

def hangman(secretWord):
    guesses = 8
    lettersGuessed = []

    print 'Welcome to the game, Hangmam!'
    print 'I am thinking of a word that is', len(secretWord) ,' letters long.'
    print '-------------'

    word = printSecretWord(secretWord, lettersGuessed)
    availableLetters = getAvailableLetters()

    while isWordGuessed(secretWord, lettersGuessed) is False and guesses > 0:
        print 'You have ', guesses, 'guesses left.'
        print 'Available letters', availableLetters
        letter = raw_input('Please guess a letter: ')

        if validLetter(letter, lettersGuessed) is True:
            if letter in secretWord:
                print 'Good Guess: '
                lettersGuessed.append(letter)
                word = printSecretWord(lettersGuessed, secretWord)
                print word

            else:
                guesses -= 1
                lettersGuessed.append(letter)
                print 'Oops! That letter is not in my word ',
        else:
                print 'Oops! You have already guessed that letter \n',

        availableLetters = updateAvailableLetter(availableLetters, lettersGuessed)
        print '------------'

    if isWordGuessed(secretWord, lettersGuessed) is True:
        print 'Congratulations, you won!'
    else:
        print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'

wordlist = loadWords()
secretWord = chooseAWord(wordlist, 8).lower()
hangman(secretWord)
