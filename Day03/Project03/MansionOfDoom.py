# Reading an archive with ASCII art
archive = open('ascii_logo.txt', 'r')
content = archive.read()
print(content)

# The main content :
print("                 -------------------")
print("          The Mansion of Doom")
print("                 -------------------")

print("Welcome to \"The Mansion of Doom,\" a text-based adventure game where you must explore a creepy mansion and uncover its dark secrets. But beware, the mansion is full of deadly traps and ghostly apparitions.\n\n")
print("Please type the number 1, 2, or 3 to choose your actions in the story.\n")

print("You are standing outside the entrance to the mansion. The gate is open, and you can hear strange noises coming from inside.")
choice = int(input(" 1 | Enter the mansion. \n 2 | Knock on the door. \n 3 | Leave and never return. \nChoice: "))
if (choice == 1):
    print("\nYou step inside the mansion, and the door slams shut behind you. You are now trapped and must find your way through the mansion to escape.")
    print("You find yourself in the foyer of the mansion. It's dark and musty, and you can barely see anything.")
    choice = int(input(" 1 | Look for a light switch. \n 2 | Call out for anyone who might be there. \n 3 | Explore the room in darkness. \nChoice: "))
    if (choice == 1):
        print("\nYou find a light switch and turn on the lights. You see a staircase leading upstairs and a hallway leading to the left.")
        print("You climb the stairs and find yourself on the second floor. You can hear strange whispers coming from one of the rooms.")
        choice = int(input(" 1 | Investigate the whispers. \n 2 | Ignore the whispers and continue exploring. \n 3 | Leave the mansion immediately. \nChoice: "))
        if (choice == 1):
            print("You investigate the whispers and find a ghostly apparition in the room. It attacks you, and you are killed. \n Game Over.")
        elif (choice == 2):
            print("\nYou ignore the whispers and continue exploring the mansion.")
            print("You find a bedroom on the second floor. It's decorated with antique furniture and a large four-poster bed.")
            choice = int(input(" 1 | Search the room for clues. \n 2 | Lie down on the bed and rest. \n 3 | Leave the room immediately. \nChoice: "))
            if (choice == 1):
                print("Y\nou explore the basement and find a hidden passage leading to a secret room.")
                print("You enter the secret room and find a mysterious object on a pedestal.")
                choice = int(input(" 1 | Take the object. \n 2 | Leave the object and look for a way out. \n 3 | Ignore the object and continue exploring. \nChoice: "))
                if (choice == 1):
                    print("As soon as you take the object, the room starts to shake, and the walls start closing in on you. You are crushed to death. Game Over.")
                elif (choice == 2):
                    print("While trying to get out of the place, you end up triggering a trap. You starved to death.Game Over.")
                elif (choice == 3):
                    print("\nYou ignore the object and continue exploring.")
                    print("You found a cute cat, what do you want to do?")
                    choice = int(input(" 1 | Kiss it forehead. \n 2 | Pat it. \n 3 | Take it. \nChoice: "))
                    if (choice == 1):
                        print("After kissing the cat's forehead, you begin to feel strange and notice that your thoughts are becoming more confused. The cat is no longer a cat, but someone dressed in a fursuit. Game Over.\n\n Yes, I know that this is not really a game over, but it got too weird for me to continue.")
                    elif (choice == 2):
                        print("You crouch down to stroke the cat, but when your hand touches its soft fur, something feels off. The cat starts purring louder and louder, as if it's enjoying the affection, but you notice its eyes are fixed on something behind you. \n You slowly turn around and see a dark figure approaching quickly. Your heart starts beating faster as you realize you're not alone there but before you could react, your own body sabotages you and you have a heart attack and die. Game Over.")
                    elif (choice == 3):
                            print("As you lift the cat, you feel a sharp pain in your hand. Looking down, you see that the cat has claws made of razor-sharp metal, and it has just sliced open your skin. You died of severe tetanus. Game Over.")
            elif (choice == 2):
                print("As you lay down to sleep, you hear someone whispering in your ear. \"I didn't know we had a sleeping beauty among us.\" And you are suffocated to death by a strange figure. Game Over.")
            elif (choice == 3):
                print("You choose leave the room immediately.")
                print("As you desperately run out of the room, you trip on the stairs and your head is pierced by a loose nail on the floor. Game Over.")
        elif(choice == 3):
             print("Leave the mansion immediately, but as you ran away from the mansion, you tripped over your own feet and hit your head on a rock, killing you instantly. Game Over, coward.")
    elif (choice == 2):
        print("You choice call out for anyone who might be there...")
        print("When calling out for someone, a trembling voice whispers, casting a curse upon you. You die not knowing what curse was responsible for your demise. Game Over.")
    elif (choice == 3):
        print("You choice explore the room in darkness")
        print("You stumble on a chair and fall to the ground, severely injuring your spine. You try to get up, but feel a sharp pain and realize that you cannot walk. You become trapped in the darkness of the room without being able to move, until you die of dehydration a few days later. Game Over.")
elif (choice == 2):
    print("You knock on the door, but no one answers. You decide to come back to the mansion at another time when someone is there to receive you.")
elif (choice == 3):
    print("You chose to flee the place and never return, but as you ran away from the mansion, you tripped over your own feet and hit your head on a rock, killing you instantly. Game Over, coward.")
    
archive.close()