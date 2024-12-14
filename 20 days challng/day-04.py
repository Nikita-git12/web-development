#Bulit in.....
import math


print(math.sqrt(16))  # Output: 4.0
print(math.factorial(5))  # Output: 120


#call...
def add(a, b):
    return a + b

print(add(5, 3))  # Output: 8


#Function
def greet(name):
    return f"Hello, {name}!"

print(greet("Nikita"))  # Output: Hello, Nikita!


#import
import module

result = my_module.multiply(4, 5)
print(result)  # Output: 20


#Module
def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed!"
