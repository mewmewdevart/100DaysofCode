print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

true_count = 0
love_count = 0

for letter in name1.upper () + name2.upper():
    if letter in 'TRUE':
        true_count += 1
    if letter in 'LOVE':
        love_count += 1

together = int(str(true_count) + str(love_count)) # Concatena as duas str e as torna int

if together < 10 or together > 90:
    print(f"Your score is {together}, you go together like coke and mentos.")
elif together >= 40 and together <= 50:
    print(f"Your score is {together}, you are alright together.")
else:
    print(f"Your score is {together}.")
