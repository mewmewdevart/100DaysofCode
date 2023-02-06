# functions with more than 1 input


def greet_with(name, age):
    print("You have a cool name " + name)
    print(f"You have a nice age {age}")


myname = input("What is your name? ")
myage = int(input("What is your age?"))

greet_with(myname, myage)


print("\n")
def greet_too(her, location):
    print(f"Hello {her}")
    print(f"You are from {location}")

greet_too(her="Angela", location="London")