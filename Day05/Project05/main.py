#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("                 -------------------")
print("     Welcome to the PyPassword Generator!")
print("                 -------------------")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

randomNumbers = []
randomSymbols = []
randomLetters = []

for i in range(nr_letters):
    letter = random.choice(letters)
    randomLetters.append(letter)

for i in range(nr_symbols):
    symbol = random.choice(symbols)
    randomSymbols.append(symbol)

for i in range(nr_numbers):
    number = random.choice(numbers)
    randomNumbers.append(number)

randomLetters = ''.join(randomLetters)
randomNumbers = ''.join(randomNumbers)
randomSymbols = ''.join(randomSymbols)

password = randomLetters + randomNumbers + randomSymbols
newPassword = ''.join(random.sample(password, len(password)))
print(f"Your password is: {newPassword}")

