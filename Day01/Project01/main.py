# Reading an archive with ASCII art
archive = open('ascii_artBand.txt', 'r')
content = archive.read()
print(content)
archive.close()

# The main content
print("                 -------------------")
print("         Welcome to the Band Name Generator.")
print("                 -------------------")
print(" 1. What's the name of the city you grew up in? ")
city_name = input("    ")
print(" 2. What's your pet's name?")
pet_name = input("    ")
print("\n        Your band name could be: " + city_name + " "+ pet_name + "!" + "\n Bro, this is so unic! \m/（  ﾟ◥益◤ﾟ）\m/")
