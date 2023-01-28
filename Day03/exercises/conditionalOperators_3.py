print("Welcome to the roller-coaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the roller-coaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Please pay $5.")
    elif age >= 12 & age <= 18:
        bill = 7
        print("Please pay $7.")
    else:
        bill = 12
        print("Please pay $12.")

    want_photo = input("Do you want pay $3 to take the photo? Y/N ")
    if (want_photo == "y") or (want_photo == "Y"):
        bill += 3

    print(f"Your final bill is : {bill}")

else:
    print("Sorry, you have to grow taller before you can ride!")
