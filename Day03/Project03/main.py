print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice = input("You're at a crossroad. Where do you want to go? Type \"left\" or \"right\" : ")

if choice == "right":
    print("You fall into a hole. Game Over.")
elif choice == "left":
    choice = input("You've come to a lake. There is an island in the middle of the lake. \n Type \"wait\"to wait for a boat. Type \"swim\" to swim across: ")
    if choice == "swim":
        print("Oh no. Attacked by trout. Game Over.")
    elif choice == "wait":
        choice = input("You arrive at the island unharmed. There is a house with 3 doors. One \"red\", one \"yellow\" and one \"blue\". Which colour do you choose? :")
        if choice == "blue":
            print("Oh no. Eaten by beasts. Game Over.")
        elif choice == "yellow":
            print("You win!")
        elif choice == "red":
            print("Burned by a fire. Game Over.")
else:
    print("Wrong option. Game Over.")