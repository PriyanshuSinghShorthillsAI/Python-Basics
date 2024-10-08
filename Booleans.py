# Boolean variables
is_sunny = True
is_raining = False

print(is_sunny)   
print(is_raining) 


is_sunny = True

if is_sunny:
    print("Let's go outside!")  
else:
    print("Stay indoors.")


x = 10
y = 20

# Comparisons return Booleans
print(x == y)   
print(x < y)   


print(True and False)  


print(True or False)  


print(not True)        


print(bool(0))         # Output: False
print(bool(1))         # Output: True
print(bool(""))        # Output: False
print(bool("Hello"))   # Output: True
print(bool([]))        # Output: False
print(bool([1, 2, 3])) # Output: True


"""
Note 1 : Values like 0, None, False, empty strings (""), empty lists ([]), etc., are evaluated as False.
Note 2: Non-empty values (like 1, non-empty strings, and non-empty lists) are evaluated as True.

"""