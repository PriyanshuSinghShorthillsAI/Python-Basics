my_dict = {
    'name': 'Alice',
    'age': 30,
    'city': 'New York'
}

# Using dict() constructor
my_dict2 = dict(name='Bob', age=25, city='Los Angeles')

print(my_dict['name'])  

print(my_dict2['age'])  


#Methods

print(my_dict.get('age', 'Not found'))  
print(my_dict.get('gender', 'Not found')) 


print(my_dict.keys())  # dict_keys(['name', 'age', 'city'])

print(my_dict.values())  # dict_values(['Alice', 30, 'New York'])

print(my_dict.items())  #  dict_items([('name', 'Alice'), ('age', 30), ('city', 'New York')])

my_dict.update({'age': 31, 'gender': 'Female'})
print(my_dict)  #  {'name': 'Alice', 'age': 31, 'city': 'New York', 'gender': 'Female'}


age = my_dict.pop('age', 'Not found')
print(age)  # Output: 31
print(my_dict)  # {'name': 'Alice', 'city': 'New York', 'gender': 'Female'}


my_dict.clear()
print(my_dict)  

# Iterating through keys
for key in my_dict2.keys():
    print(key)

# Iterating through values
for value in my_dict2.values():
    print(value)

# Iterating through key-value pairs
for key, value in my_dict2.items():
    print(f"{key}: {value}")

