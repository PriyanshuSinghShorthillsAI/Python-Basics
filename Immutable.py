name = "Priyanshu"
print(f"Original string: {name}")

# name[0] = "B"  #  will raise an error: TypeError

# Instead, we create a new string
new_name = "B" + name[1:]
print(f"Modified string: {new_name}")


# Tuple immutability
my_tuple = (1, 2, 3)
print(f"Original tuple: {my_tuple}")

# Trying to modify a tuple element (this will raise an error)
# my_tuple[0] = 10  # Uncommenting this will raise a TypeError

# Instead, create a new tuple
new_tuple = (10,) + my_tuple[1:]
print(f"Modified tuple: {new_tuple}")


# Mutable list
my_list = [1, 2, 3]
my_list[0] = 10  # Modifies the list in place
print(f"Modified list: {my_list}")  

# Immutable tuple
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  #  raise a TypeError because tuples are immutable

