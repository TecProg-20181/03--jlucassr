import random
import string
import os
from fileError import *

class HangmanGame(object):
    """ Class conatining variables and methods of HangmanGame
        to acess and execute the program.
    """

    def __init__(self, file_name='', guesses=8):

        self.guesses = guesses
        self.secretWord = ''
        self.loadWords(file_name)
        self.lettersGuessed = []


    def checkDifferentLetters(self):
        letters = set()
        letters.update(self.secretWord)
        print "The random word has been chosen and has ", len(letters), "different letters"
        return len(letters)


    def loadWords(self,file_name):
        """
            Depending on the size of the word list, this function may
            take a while to finish.
        """
        print "Loading word list from file..."
        try:
            inFile = open(file_name, 'r', 0)
            line = inFile.readline()
            wordlist = string.split(line)
            if len(wordlist) <= 0:
                raise NoErrorFromWords(file_name)
        except IOError:
            print """
                    FILE NOT FOUND.
                    See https://github.com/TecProg-20181/03--jlucassr
                    to find the respective files and put it on the same directory as hang.py and main.py"""
        except NoErrorFromWords as e:
            print e.message
        print "  ", len(wordlist), "words loaded."
        self.secretWord = random.choice(wordlist).lower()
        while self.checkDifferentLetters() > self.guesses:
            self.secretWord = random.choice(wordlist).lower()
            print "This word is too big or too difficult, another word will be chosen!"


    def isWordGuessed(self):
        for letter in self.secretWord:
            if letter in self.lettersGuessed:
                pass
            else:
                return False
            return True


    def getAvailableLetters(self):
        # 'abcdefghijklmnopqrstuvwxyz'
        available = string.ascii_lowercase
        for letter in available:
            if letter in self.lettersGuessed:
                available = available.replace(letter, '')
        return available


    def printSecretWord(self):
        word = ''
        for letter in self.secretWord:
            if letter in self.lettersGuessed:
                word += letter
            else:
                word += '_'
        return word


    def startGame(self):

        print 'Welcome to the game, Hangmam!'
        print 'I am thinking of a word that is', len(self.secretWord) ,' letters long.'
        print '-------------'

        while self.isWordGuessed() is False and self.guesses > 0:
            print 'You have ', self.guesses, 'guesses left.'
            print 'Available letters', self.getAvailableLetters()

            letter = raw_input('Please guess a letter: ')

            if letter in self.secretWord:
                self.lettersGuessed.append(letter)
                os.system('clear')
                print 'Good Guess: '

            elif len(letter) > 1:
                os.system('clear')
                print 'Guess Just One Letter, a syllable does not count!'

            elif letter in self.lettersGuessed:
                os.system('clear')
                print 'Oops! You have already guessed that letter!'

            elif letter not in self.getAvailableLetters():
                os.system('clear')
                print 'Not a Letter, Just Try Again!'

            else:
                self.guesses -= 1
                os.system('clear')
                self.lettersGuessed.append(letter)
                print 'Oops! That letter is not in my word \n',

            print self.printSecretWord()
            print '------------ \n'


        if self.isWordGuessed():
            print 'Congratulations, you won!'
        else:
            print 'Sorry, you ran out of guesses. The word was ', self.secretWord, '.'
            print 'GAME OVER \n'
