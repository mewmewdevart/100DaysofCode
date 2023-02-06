import random

# Reading an archive with ASCII art
archive = open('ascii_hangman.txt', 'r')
content = archive.read()
print(content)
archive.close()

def ft_choice_word():
    word_list = ["camel", "dolphin", "goat", "cat"]
    return random.choice(word_list)


def ft_display_word(word_list, right_word):
    display = ""
    for letter in word_list:
        if letter in right_word:
            display += letter
        else:
            display += "_"
    return display


def ft_draw_display(attempts):
    if attempts == 6:
        print(" _____")
        print("|     |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("\nThe gallows was built. Get ready to be hung!")
    elif attempts == 5:
        print(" _____")
        print("|     |")
        print("|     O")
        print("|")
        print("|")
        print("|")
    elif attempts == 4:
        print(" _____")
        print("|     |")
        print("|     O")
        print("|     |")
        print("|")
        print("|")
    elif attempts == 3:
        print(" _____")
        print("|     |")
        print("|     O")
        print("|    /|")
        print("|")
        print("|")
    elif attempts == 2:
        print(" _____")
        print("|     |")
        print("|     O")
        print("|    /|\\")
        print("|")
        print("|")
    elif attempts == 1:
        print(" _____")
        print("|     |")
        print("|     O")
        print("|    /|\\")
        print("|    / \\")
        print("|")
    elif attempts == 0:
        print(" _____")
        print("|     |")
        print("|     O")
        print("|        ")
        print("|    /|\\")
        print("|    / \\")
        print("The neck couldn't support the weight of the body...")


def game():
    letter = ft_choice_word()
    right_word = []
    wrong_word = []
    attempts = 6

    print("Welcome the Hangman Game!")
    print("The letter have", len(letter), "letters.")
    print("\n")

    while attempts > 0 and "_" in ft_display_word(letter, right_word):
        print("You have tried that word: ", wrong_word)
        print("Letter: ", ft_display_word(letter, right_word))
        print("You have ", attempts, "attempts.")

        guess = input("Try to guess one word: ").lower()

        if guess in letter:
            right_word.append(guess)
            ft_draw_display(attempts)
        else:
            wrong_word.append(guess)
            ft_draw_display(attempts)
            attempts -= 1

        print("\n")

    if "_" not in ft_display_word(letter, right_word):
        print(f"Congratulations! you guessing the word : {letter}!")
    else:
        ft_draw_display(attempts)
        print(f"Oh :( You lose! The correct word is : {letter}!")


game()
