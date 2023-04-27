print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
totalValue = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    payAge = int(input("What is your age? "))
    if (payAge <= 12):
        print("Child tickets are $5.")
        totalValue += 5
    elif (payAge <= 18):
        print("Youth tickets are $7.")
        totalValue += 7
    elif (payAge >= 45 and payAge <= 55):
        print("Free ticket!")
        totalValue = 0
    else:
        print("Adult tickets are $12.")
        totalValue += 12

    wantPhotos = input("Do you want take some photos? 'y' to yes and 'n' to no: ")
    if (wantPhotos == "y"):
        totalValue += 3
        print(f"Okay, the total bill is ${totalValue}")
    elif (wantPhotos == "n"):
        print(f"Okay, the total bill is: ${totalValue}")
    
else:
    print("Sorry, you have to grow taller before you can ride.")
