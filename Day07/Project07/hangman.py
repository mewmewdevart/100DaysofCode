import random

animals_list = ["cat", "dog", "goat", "horse", "pig", "rabbit", "buffalo", "anaconda", "bear", "bird", "fish", "tiger", "turtle", "gorilla", "ant"]

chosen_word = random.choice(animals_list)
word_length = len(chosen_word)

print(chosen_word)
display_list = []
for i in range(word_length):
    blank = '_'
    display_list.append(blank)

endGame = False
while not endGame:
    guess_player = input("Guess one letter: ").lower()
    for position in range(word_length):
        letter = chosen_word[position]
        if (letter == guess_player):
            display_list[position] = letter

    print(display_list)
    
    if "_" not in display_list:
        endGame = True
        print("You win!")