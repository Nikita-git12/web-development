#ADD....
my_list = [10, 20, 30, 40, 50]
my_list.append(60)
print(my_list)  # Output: [10, 25, 30, 40, 50, 60


#ELEMENTS....
# First element
print(my_list[0])  # Output: 10

# Last element using negative indexing
print(my_list[-1])  # Output: 50


#INSERT.....
my_list = [10, 20, 30, 40, 50]
my_list.insert(1, 15)
print(my_list)  # Output: [10, 15, 25, 30, 40, 50, 60]


#LIST.....
my_list = [10, 20, 30, 40, 50]
print(my_list)


#REMOVE....
my_list = [10, 20, 30, 40, 50]
# Remove 40
my_list.remove(40)
print(my_list)  # Output: [10, 15, 25, 30, 50, 60]

# Remove and print the last element
print(my_list.pop())  # Output: 60
print(my_list)  # Output: [10, 15, 25, 30, 50]


#SCILING....
# First three elements
print(my_list[:3])  # Output: [10, 20, 30]

# Reverse the list
print(my_list[::-1])  # Output: [50, 40, 30, 20, 10]


#UPDATE.....
my_list = [10, 20, 30, 40, 50]
my_list[1] = 25
print(my_list)  # Output: [10, 25, 30, 40, 50]
