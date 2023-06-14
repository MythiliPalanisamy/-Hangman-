import random
class Hangman:
    def __init__(self):
        self.possible_words = ['becode', 'learning', 'mathematics', 'sessions']
        self.word_to_find = [x for x in random.choice(self.possible_words)]
        self.lives = 7
        self.wrongly_guessed_letters = []
        self.turn_count = 0
        self.error_count = 0
        self.correctly_guessed_letters = '_' * len(self.word_to_find)
        self.guesses = []

        print(''' Lets play 'HANGMAN'\nRules are... \n1) You have 7 lives to guess the word. \n2) Enter a (single) letter \n(should not be a number or double letters) \n3) Guess it right and you win.\n Guess it wrong and you lose!!''')
        print('lets start...!!!')
        print(self.correctly_guessed_letters)

    def start_game(self):
        hang.play()

    def play(self):

        self.letter = input('\nGuess a letter:')
        self.turn_count += 1

        if self.letter in self.word_to_find:
            for x in range(len(self.word_to_find)):
                if self.word_to_find[x]==self.letter:
                    self.guesses[x]==self.letter


                hang.wel_played()
            else:
                hang.play()
            hang.game_over()

        else:
            print('It is wrong. try again')
            self.wrongly_guessed_letters.append(self.letter)
            self.error_count += 1
            self.lives -= 1
            hang.game_over()

    def game_over(self):
        if self.lives == 0:
            print('game over..')
            quit()
        else:

            print(f'correctly guessed letters: {self.correctly_guessed_letters}')
            print(f'wrongly guessed letters: {self.wrongly_guessed_letters}')
            print(f'lives: {self.lives}')
            print(f'error count: {self.error_count}')
            print(f'turn count: {self.turn_count}')
            hang.play()
    def wel_played(self):
        if self.correctly_guessed_letters in self.word_to_find:
            print(f'You found the word: {self.word_to_find} in {self.turn_count} turns with {self.error_count} errors!')
        else:
            hang.play()
hang=Hangman()

print(hang.start_game())
