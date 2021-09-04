# Project-Hangman-Game
#This game is being developed using python programming language
import random
from replit import clear

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

words = ["mango","apple","orange","tomato"]

chosen_word = random.choice(words)

length = len(chosen_word)

lives = 6

display = []

for _ in range(length):
  display += "_"

end_of_game = False

while not end_of_game:
  guess = input("Guess a letter : ").lower()

  clear()

  for position in range(length):
    letter = chosen_word[position]

    if letter == guess:
      display[position] = letter

  if guess not in chosen_word:
    lives -= 1
  if lives == 0:
    end_of_game = True
    print("You Loose")
  
  print(f"{' '.join(display)}")

  if "_" not in display:
        end_of_game = True
        print("You win.")

  print(stages[lives])

