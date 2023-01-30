# Go to: https://replit.com/@appbrewery/password-generator-start?v=1
import random
import string

# lists
symbols = ["[", "]", "{", "}", "☹", "★", "♥"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ]

letter = int(input("How many letters would you like in your password?"))
symbol = int(input("How many symbols would you like?"))
number = int(input("How many numbers would you like?"))

manyLetter = ""
manySymbol = ""
manyNumber = ""
calc = ""

for i in range(0, letter):
    manyLetter += random.choice(string.ascii_lowercase)

for i in range(0, symbol):
    manySymbol += random.choice(symbols)

for i in range(0, number):
    manyNumber += random.choice(numbers)

linkedElements = [manyLetter, manySymbol, manyNumber]

for i in range(0, 3):
    calc += random.choice(linkedElements)

print(calc)

