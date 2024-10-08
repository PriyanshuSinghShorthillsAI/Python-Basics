# Creating a list
fruits = ["apple", "banana", "orange", "grape"]
print(fruits)  # Output: ['apple', 'banana', 'orange', 'grape']


#Operations in List

fruits.append("mango")
print(fruits) 

fruits.insert(2, "pineapple")
print(fruits)  

fruits.remove("banana")
print(fruits)  

print(fruits[0])  


#Slicing in List

#list[start:end:step]

"""
start: The index where the slice starts (inclusive).
end: The index where the slice ends (exclusive).
step: (Optional) Determines the step or jump between elements in the slice.
"""

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Slicing from index 2 to 5 
print(numbers[2:6])  

# Slicing from the beginning to index 4
print(numbers[:5])  

# Slicing from index 5 to the end
print(numbers[5:])  

# Slicing the entire list
print(numbers[:])  


print(numbers[-3:]) 
print(numbers[:-3]) 

nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing the second list
print(nested_list[1])  

# Accessing the first element of the second list
print(nested_list[1][0])  


