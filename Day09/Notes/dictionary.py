programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

# Retrieving item from dictionary
print(programming_dictionary["Bug"])

# Adding new items to dictionary
programming_dictionary["Support"] = "Is a synonym of help"

# Print all elements in the dictionary
print(programming_dictionary)

# Print just one content in the dictionary
print(programming_dictionary["Loop"])

# Create an empty dictionary
empty_dictionary = {}

# Wipe an existing dictionary
# programming_dictionary = {}
#print(programming_dictionary)

# Edit an item in dictionary
programming_dictionary["Bug"] = "Is one insect."

print("\n")
# Loop through a dictionary
for thing in programming_dictionary:
    print(thing)
    print(programming_dictionary[thing])
