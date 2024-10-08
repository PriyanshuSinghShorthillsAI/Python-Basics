# lists_and_unpacking.py

# Create a list of fruits
fruits = ['apple', 'banana', 'cherry', 'date']

# Print the original list
print("Original list of fruits:")
print(fruits)

# Modifying the list by adding and removing items
fruits.append('elderberry')  # Adding an item
fruits.remove('banana')      # Removing an item

# Print the modified list
print("\nModified list of fruits:")
print(fruits)

# Unpacking the list into variables
first_fruit, second_fruit, *remaining_fruits = fruits

# Print the unpacked variables
print("\nUnpacking the list:")
print("First fruit:", first_fruit)
print("Second fruit:", second_fruit)
print("Remaining fruits:", remaining_fruits)

# Demonstrating the use of unpacking in a function
def print_fruit_info(first, second, *others):
    print(f"\nFirst fruit: {first}")
    print(f"Second fruit: {second}")
    print("Other fruits:", others)

# Calling the function with unpacked list
print_fruit_info(first_fruit, second_fruit, *remaining_fruits)
