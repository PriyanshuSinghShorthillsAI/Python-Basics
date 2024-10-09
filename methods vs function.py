# Function: A standalone block of code that can be called independently
def my_function():
    return "I am a function!"

# Function with parameters
def add_function(a, b):
    return a + b

# Class with methods: Methods are functions defined inside a class
class MyClass:
    
    # A method within a class (requires 'self' parameter)
    def my_method(self):
        return "I am a method inside a class!"
    
    # Method with parameters
    def multiply_method(self, a, b):
        return a * b

#  usage of functions and methods
if __name__ == "__main__":
    # Calling a function
    result_function = my_function()
    print(result_function)  # Output: I am a function!

    # Calling a function with parameters
    sum_result = add_function(5, 3)
    print(f"Sum of 5 and 3 using function: {sum_result}")  # Output: 8

    # Creating an instance of MyClass
    obj = MyClass()

    # Calling a method from an object
    result_method = obj.my_method()
    print(result_method)  # Output: I am a method inside a class!

    # Calling a method with parameters
    product_result = obj.multiply_method(4, 5)
    print(f"Product of 4 and 5 using method: {product_result}")  # Output: 20
