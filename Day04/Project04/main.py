import random
import moduleArt
import time

choices = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

computer_choice = random.choice(choices)
player_choice = int(input("What do you choose? Type:\n \t0 - Rock\n\t1 - Paper\n\t2 - Scissors\n\t3 - Lizard\n\t4 - Spock\n"))

print(f"\nPlayer choose {choices[player_choice]}")
print(f"Computer choose {computer_choice}")

# Draw Choices
def drawChoices(choice):
    if (choices[choice] == "Rock"):
        print(moduleArt.asciiArt_Rock)
    elif (choices[choice] == "Paper"):
        print(moduleArt.asciiArt_Paper)
    elif (choices[choice] == "Scissors"):
        print(moduleArt.asciiArt_Scissor)
    elif (choices[choice] == "Lizard"):
        print(moduleArt.asciiArt_Lizard)
    else:
        print(moduleArt.asciiArt_Spok)

# Batle : Actions
battle_actions = {
    ("Scissors", "Paper"): "cuts",
    ("Paper", "Rock"): "covers",
    ("Rock", "Lizard"): "crushes",
    ("Lizard", "Spock"): "poisons",
    ("Spock", "Scissors"): "smashes",
    ("Scissors", "Lizard"): "decapitates",
    ("Lizard", "Paper"): "eats",
    ("Paper", "Spock"): "disproves",
    ("Spock", "Rock"): "vaporizes",
    ("Rock", "Scissors"): "crushes",
    ("Scissors", "Rock"): "crushes",
    ("Paper", "Paper"): "nothing happens between both", # just signaling the existence
    ("Rock", "Rock"): "nothing happens between both",
    ("Lizard", "Lizard"): "nothing happens between both",
    ("Spock", "Spock"): "nothing happens between both",
}

if player_choice == choices.index(computer_choice):
    winner = 0
elif (choices[player_choice], computer_choice in battle_actions):
    winner = 1
    drawChoices(player_choice)
    print(f"\t{choices[player_choice]} {battle_actions[(choices[player_choice], computer_choice)]} {computer_choice}!")
else:
    winner = 2
    drawChoices(computer_choice)
    print(f"\t{computer_choice} {battle_actions[(computer_choice, choices[player_choice])]} {choices[player_choice]}!")

time.sleep(3)

# Score
if winner == 1:
    print("\t\tPlayer Wins!")
elif winner == 2:
    print("\t\tComputer Wins!")
else:
    print("\t\tNobody wins!")
