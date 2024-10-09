# example_args_kwargs.py

# Function that uses *args to accept variable-length arguments
def sum_numbers(*args):
    """
    Sums any number of arguments passed to the function.

    Parameters:
    *args: A variable number of positional arguments (integers or floats).

    Returns:
    int or float: The sum of all arguments.
    """
    return sum(args)


# Function that uses **kwargs to accept variable-length keyword arguments
def display_info(**kwargs):
    """
    Displays information passed as keyword arguments.

    Parameters:
    **kwargs: A variable number of keyword arguments.

    Returns:
    None
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")


# Function that uses both *args and **kwargs
def mixed_function(*args, **kwargs):
    """
    Demonstrates the use of both *args and **kwargs.

    Parameters:
    *args: A variable number of positional arguments.
    **kwargs: A variable number of keyword arguments.

    Returns:
    None
    """
    print("Positional arguments (*args):", args)
    print("Keyword arguments (**kwargs):", kwargs)


if __name__ == "__main__":
    # Calling sum_numbers function with *args
    result = sum_numbers(1, 2, 3, 4, 5)
    print(f"Sum of numbers: {result}")

    # Calling display_info function with **kwargs
    display_info(name="Priyanshu", age=25, city="Bangalore")

    # Calling mixed_function with both *args and **kwargs
    mixed_function(10, 20, 30, name="Priyanshu", role="SDE1")
