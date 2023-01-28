# Reading an archive with ASCII art
archive = open('ascii_artTip.txt', 'r')
content = archive.read()
print(content)
archive.close()

# The main content
print("                 -------------------")
print("         Welcome to the tip calculator!")
print("                 -------------------")
bill = float(input(" What was the total bill? $"))
tip = int(input(" How much tip would you like to give? 10, 12, or 15? "))
split = int(input(" How many people to split the bill? "))

tip_convert = tip/100
tip_total = bill * tip_convert
bill_total = bill + tip_total
bill_person = bill_total / split

print(f" Each person should pay: ${round(bill_person, 2)}")