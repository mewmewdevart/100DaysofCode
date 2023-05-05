#   def my_functions(something);
        #Do this something
        #Then do this
        #Finally do this

# my_funcion(something)

# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# Simple function
def greet():
    print("Great!")
    print("Awesome!")
    print("Lovely!")

greet()

print("-------------")

# Function that allows for input
def gree_with_name(name):
    print(f"Hello {name}!")
    print(f"How are you, {name}")

gree_with_name("Larissa")

print("-------------")
# Function with more than 1 input
def gree_with(name, location):
    print(f"Hello {name}")
    print(f"Are you from {location}?")

gree_with("Larissa", "Brazil")

print("-------------")
# Function with more than 1 input
def gree_with(name="Joao", location="Brazil"):
     print(f"Hello {name}")
     print(f"Is he from {location}?")
     
gree_with()


