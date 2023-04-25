# Reading an archive with ASCII art
archive = open('ascii_artTip.txt', 'r')
content = archive.read()
print(content)

# The main content :

print("                 -------------------")
print("          Welcome to the tip calculator!")
print("                 -------------------")

bill = float(input("What was the total bill? "))
tip = int(input("How much tip would you like to give? 10, 12, or 15: "))
split = int(input("How many people to split the bill? "))

# To check if is a valid tip
if tip == 10:
    tip = 1.10
elif tip == 12:
    tip = 1.12
elif tip == 15: 
    tip = 1.15
else:
    print("Please, inset a correct tip %!")

needPay = round((bill/split) * tip, 2)

print(f"Earch person should pay: ${needPay}!")

archive.close()
