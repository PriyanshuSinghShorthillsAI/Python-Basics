def my_function():
    pass  

result = my_function()
print(result)  # Output: None


my_var = None

if my_var is None:
    print("my_var has no value")  


def greet(name=None):
    if name is None:
        print("Hello, Guest!")
    else:
        print(f"Hello, {name}!")

greet()         
greet("Alice")  


data = {
    'name': 'John',
    'age': None,  
    
}


print(None == False)  # Output: False
print(None == 0)      # Output: False
print(None == "")     # Output: False


"""
Note 1: Default Return Value: Functions in Python that do not explicitly return a value will return None by default. 
Note 2: Conditional Checks: You can use None in conditional statements to check if a variable is uninitialized or has no value.
Note 3: Function Parameters: None is commonly used as a default value for function parameters. This allows for optional parameters in function definitions.
Note 4: Representing Null or Empty Values: In data structures like lists, dictionaries, or custom objects, None can be used to represent missing or undefined data.
Note 6: Comparing with Other Types: None is unique and is not equal to any other data type, including False, 0, or an empty string. It is considered to be a distinct type of its own.

"""