""" Calls the HangmanGame
"""

from hang import HangmanGame

WORDLIST_FILENAME = "words.txt"
NUMBER_OF_GUESSES = 8

GAME = HangmanGame(file_name=WORDLIST_FILENAME, guesses=NUMBER_OF_GUESSES)
GAME.startGame()
