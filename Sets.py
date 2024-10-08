# sets_example.py

# Creating Sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Set 1:", set1)
print("Set 2:", set2)

# Creating an empty set
empty_set = set()
print("Empty Set:", empty_set)

# Adding elements to a set
set1.add(5)
print("Set 1 after adding 5:", set1)

# Updating a set with multiple elements
set1.update([6, 7, 8])
print("Set 1 after update:", set1)

# Removing an element
set1.remove(2)
print("Set 1 after removing 2:", set1)

# Discarding an element (does not raise an error if the element is not found)
set1.discard(10)  # No error will be raised
print("Set 1 after discarding 10 (not found):", set1)

# Pop an element (removes and returns an arbitrary element)
popped_element = set1.pop()
print("Popped element:", popped_element)
print("Set 1 after popping an element:", set1)

# Set operations: Union, Intersection, Difference
union_set = set1.union(set2)
print("Union of Set 1 and Set 2:", union_set)

intersection_set = set1.intersection(set2)
print("Intersection of Set 1 and Set 2:", intersection_set)

difference_set = set1.difference(set2)
print("Difference of Set 1 and Set 2:", difference_set)

# Checking membership
print("Is 3 in Set 1?", 3 in set1)
print("Is 10 in Set 1?", 10 in set1)

# Iterating through a set
print("Iterating through Set 1:")
for element in set1:
    print(element)

# Converting a list to a set to remove duplicates
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(my_list)
print("Unique elements from the list:", unique_set)
