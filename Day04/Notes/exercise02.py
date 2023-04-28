import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

len_list = len(names) - 1
random_names = random.randint(0, len_list)

print(f"{names[random_names]} is going to buy the meal today!") # take the random position
