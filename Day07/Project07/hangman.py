import random
import moduleList

choice_list = -1
print("Welcome to Hangman!")

while choice_list == -1:
    try:
        choice_list = int(input("What kind of thing do you want to guess? Type:\n \t0 - Animal\n\t1 - Object\n\t2 - Famous\n"))
    except ValueError:
        print("It is not a valid choice! Please try insert one valid number again.")
        exit()
    else:
        if (choice_list == 0):
            chosen_word = random.choice(moduleList.animals_list)
            print("Choice: animal. You will have to guess an animal.")
        elif (choice_list == 1):
            chosen_word = random.choice(moduleList.animals_list)
            print("Choice: animal. You will have to guess an animal.")
        elif(choice_list == 2):
            chosen_word = random.choice(moduleList.animals_list)
            print("Choice: animal. You will have to guess an animal.")

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