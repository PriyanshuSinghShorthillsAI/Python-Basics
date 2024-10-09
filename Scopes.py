# example_scope.py

# Global variable
x = 10

def outer_function():
    """
    Demonstrates local and nonlocal scope.
    """
    x = 20  # This x is in the local scope of outer_function

    def inner_function():
        nonlocal x  # Refers to the x in the outer_function scope
        x = 30  # Changes the nonlocal x
        print(f"Inner function, x: {x}")  # x = 30

    inner_function()
    print(f"Outer function, x: {x}")  # x = 30 after modification in inner_function


def global_scope_example():
    """
    Demonstrates global scope.
    """
    global x  # Refers to the global variable x
    x = 50  # Changes the global x
    print(f"Global scope, x: {x}")  # x = 50


if __name__ == "__main__":
    # Accessing the global variable
    print(f"Global x before any function call: {x}")  # x = 10

    # Demonstrating local and nonlocal scope
    outer_function()  # Will print x values from local and nonlocal scopes

    # Accessing the global variable again to see if it changed
    print(f"Global x after outer_function: {x}")  # x = 10, global x is unchanged

    # Demonstrating global scope modification
    global_scope_example()

    # Checking global x after modification by global_scope_example
    print(f"Global x after global_scope_example: {x}")  # x = 50, global x is modified
