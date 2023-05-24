from asciiArt import calculatorDesign

def addition(n1, n2):
    return n1 + n2

def subtraction(n1, n2):
    return n1 - n2

def division(n1, n2):
    return n1 / n2

def multiplication(n1, n2):
    return n1 * n2

operationsSignals = {
    "+": addition,
    "-": subtraction,
    "*": multiplication,
    "/": division
}

print("\t Welcome to MyCalculator!")
print(" This is an interactive calculator program.\n")
fNumber = int(input("What's the first number?: "))

print("\t ------------")
print(calculatorDesign)
print(" Addition (+)")
print(" Subtraction (-)")
print(" Multiplication (*)")
print(" Division (/)\n")

sNumber = int(input("What's the second number?: "))

operationsResult = input(" Pick an operation from the line above: ")
print("\t ------------")
calculation = operationsSignals[operationsResult]
first_answer = calculation(fNumber, sNumber)
print(f" Calculation result: {fNumber} {operationsResult} {sNumber} = {first_answer}")

while True:
    continueCalculating = input("Do you want to continue calculating? Type 'y' or 'n': ")
    if continueCalculating == "y":
        operationsResult = input("Pick an operation from the line above: ")
        num3 = int(input("What's the next number? "))
        print("\t ------------")
        calculation = operationsSignals[operationsResult]
        second_answer = calculation(first_answer, num3)
        print(f"Calculation result: {first_answer} {operationsResult} {num3} = {second_answer}")
        first_answer = second_answer
    else:
        break

print("Closing the calculator!")
