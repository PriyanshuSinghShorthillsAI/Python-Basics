# example_docstring.py

def add_numbers(a, b):
    """
    Adds two numbers together.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The sum of the two numbers.
    """
    return a + b


def greet_user(name="Guest"):
    """
    Greets the user by their name.

    Parameters:
    name (str): The name of the user (default is "Guest").

    Returns:
    None
    """
    print(f"Hello, {name}!")


class Calculator:
    """
    A simple calculator class to perform basic arithmetic operations.
    """

    def multiply(self, x, y):
        """
        Multiplies two numbers.

        Parameters:
        x (int or float): The first number.
        y (int or float): The second number.

        Returns:
        int or float: The product of the two numbers.
        """
        return x * y


if __name__ == "__main__":
    # Calling the functions
    sum_result = add_numbers(10, 5)
    print(f"Sum: {sum_result}")

    greet_user("Priyanshu")

    # Creating an object of Calculator and calling the method
    calc = Calculator()
    product_result = calc.multiply(4, 3)
    print(f"Product: {product_result}")

    # Accessing docstrings
    print("\nFunction 'add_numbers' docstring:")
    print(add_numbers.__doc__)

    print("\nClass 'Calculator' docstring:")
    print(Calculator.__doc__)

    print("\nMethod 'multiply' docstring:")
    print(Calculator.multiply.__doc__)
