# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

len_size = len(names) - 1
random_names = random.randint(0, len_size)

print(f"{names[random_names]} is going to buy the meal today!")
