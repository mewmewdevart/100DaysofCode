import random
import moduleList
import time
from asciiArt import hangmanpics
from asciiArt import trophy

choice_list = -1 # initialize the variable with an invalid choice value

print("\t\t\t-----------------------")
print("\t\t\tWelcome to Hangman Game!		")
print("\t\t\t-----------------------")

print(" Guess the phrase before the drawing of the hanged man is completed. \n \tWith each incorrect guess, the drawing of the hanged man approaches its end.")
print("\t\t\t\t------")

while choice_list == -1:
	try:
		choice_list = int(input("What kind of thing do you want to guess? Type:\n\t0 - Animal\n\t1 - Object\n\t2 - Countries\n\t3 - Planets\n\t4 - Colors\n I choose the number: "))
	except ValueError:
		print("It is not a valid choice! Please try inserting a valid number again.")
		choice_list = -1 # reset the value to -1 to ask for input again
	else:
		if (choice_list == 0):
			chosen_word = random.choice(moduleList.animals_list)
			print("Category: Animal. You will have to guess an animal.")
		elif (choice_list == 1):
			chosen_word = random.choice(moduleList.objects_list)
			print("Category: Object. You will have to guess an object.")
		elif(choice_list == 2):
			chosen_word = random.choice(moduleList.countries_list)
			print("Category: Country. You will have to guess a country.")
		elif(choice_list == 3):
			chosen_word = random.choice(moduleList.planets_list)
			print("Category: Planet. You will have to guess a planet.")
		elif(choice_list == 4):
			chosen_word = random.choice(moduleList.colors_list)
			print("Category: Color. You will have to guess a color.")
		else:
			print("It is not a valid choice! Please try inserting a valid number again.\n")
			choice_list = -1 # reset the value to -1 to ask for input again

for i in range(1, 4):
	print(f"\tThe game will start in {i} seconds..")
	time.sleep(1)

word_length = len(chosen_word)

display_list = []
for i in range(word_length):
	blank = '_'
	display_list.append(blank)

print("\n\t\t---------\n")
print(f"The word you need to guess has {word_length} letters.")

chosen_word = chosen_word.lower()
print(chosen_word)
print(display_list)

lifeGame = 6
draw = 1

endGame = False
while not endGame:
	if draw:
		print(hangmanpics[draw])
  
	guess_player = input("Guess one letter: ").lower()
	checker = 0
	for position in range(word_length):
		letter = chosen_word[position]
		if (letter == guess_player):
			display_list[position] = letter
			checker = 1

	if (checker == 0):
		lifeGame -= 1
		draw += 1

	if (lifeGame == 0):
		print("Oh no, you lose!")
		break

	print("\n\t---------")
	print(display_list)
	
	if "_" not in display_list:
		endGame = True
		print("\n\t---------")
		print("\nCongratulations, you win!")
		print(trophy[0])