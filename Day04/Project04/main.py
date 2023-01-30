import random
import time

# Reading an archive with ASCII art
archiveRock = open('rock.txt', 'r')
Print_rock = archiveRock.read()
archiveRock.close()

archivePaper = open('paper.txt', 'r')
Print_paper = archivePaper.read()
archivePaper.close()

archiveScissor = open('scissor.txt', 'r')
Print_scissor= archiveScissor.read()
archiveScissor.close()

archiveLizard = open('lizard.txt', 'r')
Print_lizard= archiveLizard.read()
archiveLizard.close()

archiveSpok = open('spok.txt', 'r')
Print_spok = archiveSpok.read()
archiveSpok.close()

print("Welcome to \"Rock, Paper or Scissors Game\"!")

print("What do you choose? Type:\n")
print("\t0 - Rock\n\t1 - Paper\n\t2 - Scissors\n\t3 - Lizard\n\t4 - Spock\n")
player = int(input("\tI want choose: "))
computer = random.randint(0, 4)

# Variables
rock = 0
paper = 1
scissor = 2
lizard = 3
spock = 4
countPlayer = 0
countComputer = 0

# check print
print("\n")
if player == 0:
    print("\tPlayer choice rock!")
elif player == 1:
    print("\tPlayer choice paper!")
elif player == 2:
    print("\tPlayer choice scissor!")
elif player == 3:
    print("\tPlayer choice lizard!")
elif player == 4:
    print("\tPlayer choice spock!")

if computer == 0:
    print("\tComputer choice rock!")
elif computer == 1:
    print("\tComputer choice paper!")
elif computer == 2:
    print("\tComputer choice scissor!")
elif computer == 3:
    print("\tComputer choice lizard!")
elif computer == 4:
    print("\tComputer choice spock!")



# Player Actions
if player == scissor and computer == paper:
    print(Print_scissor)
    print("\tScissors cuts Paper!")
    countPlayer += 1
elif player == paper and computer == rock:
    print(Print_paper)
    print("\tPaper covers Rock!")
    countPlayer += 1
elif player == rock and computer == lizard:
    print(Print_rock)
    print("\tRock crushes Lizard")
    countPlayer += 1
elif player == lizard and computer == spock:
    print(Print_lizard)
    print("\tLizard poisons Spock")
    countPlayer += 1
elif player == spock and computer == scissor:
    print(Print_spok)
    print("\tSpock smashes Scissors")
    countPlayer += 1
elif player == scissor and computer == lizard:
    print(Print_scissor)
    print("\tScissors decapitates Lizard! ")
    countPlayer += 1
elif player == lizard and computer == paper:
    print(Print_lizard)
    print("\tLizard eats Paper!")
    countPlayer += 1
elif player == paper and computer == spock:
    print(Print_paper)
    print("\tPaper disproves Spock!")
    countPlayer += 1
elif player == spock and computer == rock:
    print(Print_spok)
    print("\tSpock vaporizes Rock!")
    countPlayer += 1
elif player == rock and computer == scissor:
    print(Print_rock)
    print("\tRock crushes Scissors!")
    countPlayer += 1

# Computer Actions
if computer == scissor and player == paper:
    print(Print_scissor)
    print("\tScissors cuts Paper!")
    countComputer += 1
elif computer == paper and player == rock:
    print(Print_paper)
    print("\tPaper covers Rock!")
    countComputer += 1
elif computer == rock and player == lizard:
    print(Print_rock)
    print("\tRock crushes Lizard")
    countComputer += 1
elif computer == lizard and player == spock:
    print(Print_lizard)
    print("\tLizard poisons Spock")
    countComputer += 1
elif computer == spock and player == scissor:
    print(Print_spok)
    print("\tSpock smashes Scissors")
    countComputer += 1
elif computer == scissor and player == lizard:
    print(Print_scissor)
    print("\tScissors decapitates Lizard! ")
    countComputer += 1
elif computer == lizard and player == paper:
    print(Print_lizard)
    print("\tLizard eats Paper!")
    countComputer += 1
elif computer == paper and player == spock:
    print(Print_paper)
    print("\tPaper disproves Spock!")
    countComputer += 1
elif computer == spock and player == rock:
    print(Print_spok)
    print("\tSpock vaporizes Rock!")
    countComputer += 1
elif computer == rock and player == scissor:
    print(Print_rock)
    print("\tRock crushes Scissors!")
    countComputer += 1

time.sleep(3)

# Check the winner
if countPlayer == 1:
    print("\t \tPlayer Win!")
elif countComputer == 1:
    print("\t \tComputer Win!")
else:
    print("\\ttNobody won!")
