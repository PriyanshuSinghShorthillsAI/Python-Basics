# example_global_nonlocal.py

# Global variable
counter = 0

def increment_global():
    """
    Demonstrates the use of the global keyword.
    Modifies the global variable 'counter'.
    """
    global counter  # Refers to the global variable 'counter'
    counter += 1
    print(f"Global counter: {counter}")


def outer_function():
    """
    Demonstrates the use of the nonlocal keyword.
    Modifies a variable in the enclosing function's scope.
    """
    count = 10  # Local to outer_function

    def inner_function():
        nonlocal count  # Refers to the 'count' in outer_function's scope
        count += 5
        print(f"Nonlocal count in inner_function: {count}")

    inner_function()
    print(f"Nonlocal count in outer_function after inner_function: {count}")


if __name__ == "__main__":
    # Demonstrating global keyword
    print("Before incrementing global counter:")
    print(f"Initial global counter: {counter}")
    increment_global()
    increment_global()

    # Demonstrating nonlocal keyword
    print("\nBefore modifying nonlocal variable:")
    outer_function()
