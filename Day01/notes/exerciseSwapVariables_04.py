# Write a program that switches the values stored in the variables a and b.

a = input("a: ")
b = input("b: ")

swap = a
a = b
b = swap

print("a: " + a)
print("b: " + b)