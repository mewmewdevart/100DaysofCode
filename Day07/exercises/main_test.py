import random


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


word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

display = []
for _ in range(word_length):
    display += "_"

end_of_game = False
while  end_of_game == False:
    guess = input("Guess a letter: ").lower()

    # check the guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")

    # Join all the elements
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")

        print(stages[lives])
