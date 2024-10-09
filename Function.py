def greet():
    print("Hello! Welcome to the function example.")

# A function with parameters to add two numbers
def add_numbers(a, b):
    return a + b

# A function with default parameters
def greet_user(name="Guest"):
    print(f"Hello, {name}!")
# A function that returns multiple values
def get_min_max(numbers):
    return min(numbers), max(numbers)

# Main code to call the functions
if __name__ == "__main__":
    # Call the greet function
    greet()
    
    # Call the add_numbers function
    result = add_numbers(5, 3)
    print(f"Sum of 5 and 3 is: {result}")
    
    # Call the greet_user function with and without an argument
    greet_user("Priyanshu")
    greet_user()
    
    # Call the get_min_max function
    nums = [10, 2, 30, 4, 50]
    minimum, maximum = get_min_max(nums)
    print(f"Minimum: {minimum}, Maximum: {maximum}")
