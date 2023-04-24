f = open('bandLogo.txt', 'r')
content = f.read()
print(content)

print("Welcome to a Band Name Generator!")
cityName = input("What is the name of the city you grew up in? ")
petName = input("What is the name of your pet? ")
bandName = cityName + " " + petName
print("Your band name is: " + bandName + ". It sounds great, dude!")

f.close()