def prime_checker(number):
    if (number < 2):
        print("It's not a prime number.")
    elif (number == 2):
        print("It's a prime number.")
    elif ((number%2) == 0):
        print("It's not a prime number.")
    else:
        for i in range(3, round((number**0.5)//1) + 1, 2):
            if (number%i) == 0:
                print("It's not a prime number.")
                return
        print("It's a prime number.")
    
n = int(input("Check this number: "))
prime_checker(number=n)
