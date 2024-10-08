# indentation_example.py

# Function to check if a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")

# Function to demonstrate nested indentation
def nested_indentation_example(num):
    if num > 0:
        print(f"{num} is a positive number.")
        if num % 2 == 0:
            print(f"{num} is also even.")
        else:
            print(f"{num} is also odd.")
    else:
        print(f"{num} is a negative number or zero.")

# Main block to test the functions
if __name__ == "__main__":
    # User input for checking even or odd
    number = int(input("Enter a number to check if it is even or odd: "))
    check_even_odd(number)

    # User input for nested indentation example
    nested_number = int(input("Enter a number for the nested example: "))
    nested_indentation_example(nested_number)

    # Demonstrating the importance of indentation
    try:
        # This code block will demonstrate an intentional indentation error
        if True:
            print("This will raise an IndentationError")
    except IndentationError as e:
        print("An IndentationError occurred:", e)
