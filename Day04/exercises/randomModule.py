import random #random module
import my_module

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random() # print um numero flutuante entre 0.0 e 1.0
print(random_float)

random_float_2 = random.uniform(0,5) # printando um numero aleatorio flutuante entre 0 e 5
print(random_float_2)

print(my_module.a)