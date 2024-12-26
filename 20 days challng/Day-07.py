# Dict_access......
my_dict = {"name": "Nikita", "age": 19}
print(my_dict["name"])  # Output: Nikita
print(my_dict.get("age"))  # Output: 19
print(my_dict.get("gender", "Female"))  # Output: Female


#Dict_adding.....
my_dict = {"name": "Karan"}
update_data = {"age": 19, "city": "Siliguri"}
my_dict.update(update_data)  # Merges dictionaries
print(my_dict)  # Output: {'name': 'Karan', 'age':19, 'city': 'Siliguri'}


#Dict_checking
my_dict = {"name": "Diya", "age": 19}
print("name" in my_dict)  # Output: True
print("gender" in my_dict)  # Output: False


#Dict_clearing
my_dict = {"name": "Gungun", "age": 18}
my_dict.clear()  # Removes all items
print(my_dict)  # Output: {}


#Dict_copy
my_dict = {"name": "Mohini", "age": 19}
new_dict = my_dict.copy()
print(new_dict)  # Output: {'name': 'Mohini', 'age': 19}


#Dict_delete
my_dict = {"name": "Iksha", "age": 19}
my_dict.pop("age")  # Removes 'age' key
print(my_dict)  # Output: {'name': 'Iksha'}

del my_dict["name"]  # Deletes 'name' key
print(my_dict)  # Output: {}


#Dict_itering.......
my_dict = {"name": "Nikita", "age": 19}

# Iterating through keys
for key in my_dict.keys():
    print(key)  # Output: name, age

# Iterating through values
for value in my_dict.values():
    print(value)  # Output: Nikita, 19

# Iterating through key-value pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")  # Output: name: Nikita, age: 19


#Dict_nested......
students = {
    "101": {"name": "Nikita", "age": 19},
    "102": {"name": "Diya", "age": 19}
}

# Accessing nested data
print(students["101"]["name"])  # Output: Nikita


#Dict_update
my_dict = {"name": "Nikita"}
my_dict["age"] = 19  # Adding a new key-value pair
my_dict["name"] = "Rani"  # Updating an existing key-value pair
print(my_dict)  # Output: {'name': 'Rani', 'age': 19}











