import math

"""
You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

number of cans = (wall height x wall width) ÷ coverage per can.

e.g. Height = 2, Width = 4, Coverage = 5

number of cans = (2 * 4) / 5

                           = 1.6
"""

def paint_wall(width, height, cover):
    result = math.ceil((height*width)/cover)
    print(f"You'll need {result} cans of paint.")

cover = 5
height = int(input("Height of wall: "))
width = int(input("Width of wall: "))

paint_wall(width, height, cover)
