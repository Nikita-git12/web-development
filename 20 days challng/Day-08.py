#Set_adding.....
set1 = {1, 2, 3, 4}
set1.add(5)
print(set1)  # Output: {1, 2, 3, 4, 5}


#Set_clear.....
set1 = {1, 2, 3, 4}
set1.clear()
print(set1)  # Output: set()


#Set_cpoy.....
set1 = {1, 2, 3, 4}
set1.clear()
print(set1)  # Output: set()


#Set_create.....
# Creating sets
set1 = {1, 2, 3, 4}
set2 = set([3, 4, 5, 6])  # Using the set() constructor
print(set1)  # Output: {1, 2, 3, 4}
print(set2)  # Output: {3, 4, 5, 6}


#Set_difference.....
# Creating sets
set1 = {1, 2, 3, 4}
set2 = set([3, 4, 5, 6])  # Using the set() constructor
print(set1)  # Output: {1, 2, 3, 4}
print(set2)  # Output: {3, 4, 5, 6}


#Set_intersection.....
set1 = {1, 2, 3, 4}
set2 = set([3, 4, 5, 6])  
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3, 4}


#Set_length.....
set1 = {1, 2, 3, 4}
set2 = set([3, 4, 5, 6])
print(len(set2))  # Output: 4


#Set_remove.....
set1 = {1, 2, 3, 4}
set1.remove(2)  # Removes 2, throws an error if not found
print(set1)  # Output: {1, 3, 4, 5}

set1.discard(6)  # Safely removes 6, no error if not found
print(set1)  # Output: {1, 3, 4, 5}


#Set_subset.....
set1 = {1, 2, 3, 4}
set2 = set([3, 4, 5, 6])
subset = {3, 4}
print(subset.issubset(set2))  # Output: True
print(set2.issuperset(subset))  # Output: True


#Set_symmetric-diff.....
set1 = {1, 2, 3, 4}
set2 = set([3, 4, 5, 6])  
symmetric_diff = set1.symmetric_difference(set2)
print(symmetric_diff)  # Output: {1, 2, 5, 6}


#Set_union.....
set1 = {1, 2, 3, 4}
set2 = set([3, 4, 5, 6])  
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5, 6}
