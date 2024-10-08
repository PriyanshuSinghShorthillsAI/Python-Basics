# tuples_example.py

# Creating Tuples
my_tuple = (1, 2, 3)
print("Tuple:", my_tuple)

# Creating a tuple with mixed data types
mixed_tuple = (1, "apple", 3.14, [2, 4])
print("Mixed Tuple:", mixed_tuple)

# Creating a single element tuple
single_element_tuple = (5,)
print("Single Element Tuple:", single_element_tuple)

# Creating an empty tuple
empty_tuple = ()
print("Empty Tuple:", empty_tuple)

# Accessing Tuple Elements
print("First element:", my_tuple[0])
print("Slice of Tuple:", my_tuple[1:3])

# Using count() method
count_tuple = (1, 2, 1, 3, 1)
print("Count of 1 in count_tuple:", count_tuple.count(1))  # Output: 3

# Using index() method
print("Index of first occurrence of 2:", count_tuple.index(2))  # Output: 1

# Nested Tuples
nested_tuple = ((1, 2), (3, 4), (5, 6))
print("Nested Tuple:", nested_tuple)

# Unpacking a Tuple
a, b, c = (10, 20, 30)
print("Unpacked values:", a, b, c)

# Returning multiple values from a function using tuples
def get_name_age():
    return ("Alice", 30)

name, age = get_name_age()
print("Name:", name, "| Age:", age)

# Iterating through a Tuple
print("Iterating through a tuple:")
for item in my_tuple:
    print(item)

# Demonstrating tuple as dictionary key
my_dict = {my_tuple: "This is my tuple key"}
print("Dictionary with tuple key:", my_dict)
