# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
result_height = float(height) * float(height)
calc = int(weight) / result_height

print(int(calc))