# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
totalCount = 0

if (size == "S"):
    totalCount += 15
    if (add_pepperoni == "Y"):
        totalCount += 2
    if (extra_cheese == "Y"):
        totalCount += 1
elif (size == "M"):
    totalCount += 20
    if (add_pepperoni == "Y"):
        totalCount += 3
    if (extra_cheese == "Y"):
        totalCount += 1
elif (size == "L"):
    totalCount += 25
    if (add_pepperoni == "Y"):
        totalCount += 3
    if (extra_cheese == "Y"):
        totalCount += 1
else:
    print("Please, choose a valid size!")

if (size == "S" or size == "M" or size == "L" ):
    print(f"Your final bill is: ${totalCount}")

