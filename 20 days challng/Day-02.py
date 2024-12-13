#ARITHMETIC.....

a, b = 10, 3

print("Addition:", a + b)           # Output: 13
print("Subtraction:", a - b)        # Output: 7
print("Multiplication:", a * b)     # Output: 30
print("Division:", a / b)           # Output: 3.333...
print("Floor Division:", a // b)    # Output: 3
print("Modulus:", a % b)            # Output: 1
print("Exponentiation:", a ** b)    # Output: 1000



#COMPARISON......
x, y = 5, 8

print("x == y:", x == y)  # Output: False
print("x != y:", x != y)  # Output: True
print("x > y:", x > y)    # Output: False
print("x < y:", x < y)    # Output: True
print("x >= y:", x >= y)  # Output: False
print("x <= y:", x <= y)  # Output: True



#DATA TYPES....

# String
my_string = "Hello, Python!"
print(my_string, type(my_string))  # Output: Hello, Python! <class 'str'>

# Boolean
my_bool = True
print(my_bool, type(my_bool))  # Output: True <class 'bool'>

# List
my_list = [1, 2, 3, "Python"]
print(my_list, type(my_list))  # Output: [1, 2, 3, 'Python'] <class 'list'>

# Tuple
my_tuple = (1, 2, 3)
print(my_tuple, type(my_tuple))  # Output: (1, 2, 3) <class 'tuple'>

# Dictionary
my_dict = {"name": "Nikita", "age": 19}
print(my_dict, type(my_dict))  # Output: {'name': 'Nikita', 'age': 19} <class 'dict'>

# Set
my_set = {1, 2, 3}
print(my_set, type(my_set))  # Output: {1, 2, 3} <class 'set'>



#LOGICAL

a, b = True, False

print("a and b:", a and b)  # Output: False
print("a or b:", a or b)    # Output: True
print("not a:", not a)      # Output: False
