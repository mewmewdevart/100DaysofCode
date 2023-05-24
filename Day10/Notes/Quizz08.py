Pergunta 1:
Without running the code below, what do you think will be printed in the console?

def add(n1, n2):
  return n1 + n2
 
def subtract(n1, n2):
  return n1 - n2
 
def multiply(n1, n2):
  return n1 * n2
 
def divide(n1, n2):
  return n1 / n2
 
print(add(2, multiply(5, divide(8, 4))))

Answer: 12.0

Pergunta 2:
What would you predict to be the result of running the following code?

def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)

Answer: 15

Pergunta 3:
What will be printed in the console after running the following code?

def my_function(a):
    if a < 40:
        return
        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"
print(my_function(25))

Answer : None
