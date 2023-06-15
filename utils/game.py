#import random and sys module
import random
import sys

class Hangman:

    #initialising attributes
    def __init__(self):
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find = [x for x in random.choice(self.possible_words)]
        self.lives = 7
        self.wrongly_guessed_letters = []
        self.turn_count = 0
        self.error_count = 0
        self.correctly_guessed_letters = '_' * len(self.word_to_find)
        self.guesses = ['_'] * len(self.word_to_find)

    def play(self):
        letter = input('\nGuess a letter:').lower()
        self.turn_count += 1

        if letter in self.word_to_find:
            for i, x in enumerate(self.word_to_find):
                if x == letter and self.word_to_find[i] not in self.guesses[i]:
                    self.guesses.pop(i)
                    self.guesses.insert(i,x)
                    self.correctly_guessed_letters="".join(self.guesses)
                    Hangman.game_over(self)

        elif letter not in self.word_to_find:
            self.wrongly_guessed_letters.append(letter)
            self.error_count += 1
            self.lives -= 1
            Hangman.game_over(self)

    #starting game
    def start_game(self):
        print(''' Lets play 'HANGMAN'\nRules are... \n1) You have 7 lives to guess the word. \n2) Enter a (single) letter \n(should not be a number or double letters) \n3) Guess it right and you win.\n Guess it wrong and you lose!!''')
        print('lets start...!!!')
        print(self.correctly_guessed_letters)
        Hangman.play(self)

    #possibilities for game over    
    def game_over(self):
        if self.guesses == self.word_to_find:
            Hangman.wel_played(self)

        if self.lives == 0:
            print('game over..')
            sys.exit()

        elif self.lives > 0:
            print('It is wrong. try again')
            print(f'correctly guessed letters: {self.correctly_guessed_letters}')
            print(f'wrongly guessed letters: {self.wrongly_guessed_letters}')
            print(f'lives: {self.lives}')
            print(f'error count: {self.error_count}')
            print(f'turn count: {self.turn_count}')
            Hangman.play(self)

    #winning result
    def wel_played(self):
        print(f'You found the word: "{self.correctly_guessed_letters}" in {self.turn_count} turns with {self.error_count} errors!')
        print('you WON!!! you are the WINNER!!!')
        sys.exit()
hang=Hangman()

print(hang.start_game())
