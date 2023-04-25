num_char = len(input("What is your name? "))
# print("Your name has " + (str)num_char + " character.") # you only can concatenate strings or do casting
# print("Your name has " + (str)num_char + " character.")

print(type(num_char)) # Verifica e printa o tipo da variavel

new_num_char = str(num_char)

print(type(new_num_char))

print("Your name has " + new_num_char + " character.")

# Types of casting variable
float(123)
str(123)
int(123)

print(70 + float("100.5"))

print(str(70) + str(100))
