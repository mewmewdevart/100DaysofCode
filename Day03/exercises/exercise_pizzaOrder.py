# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

if size == "S":
    cust = 15
    if add_pepperoni == "Y":
        cust += 2
        if extra_cheese == "Y":
            cust += 1
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            cust += 1
    print(f"Your final bill is: ${cust}")
elif size == "M":
    cust = 20
    if add_pepperoni == "Y":
        cust += 3
        if extra_cheese == "Y":
            cust += 1
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            cust += 1
    print(f"Your final bill is: ${cust}")
elif size == "L":
    cust = 25
    if add_pepperoni == "Y":
        cust += 3
        if extra_cheese == "Y":
            cust += 1
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            cust += 1
    print(f"Your final bill is: ${cust}")
