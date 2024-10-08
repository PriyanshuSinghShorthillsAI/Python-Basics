# logical_operators_example.py

# Function to demonstrate logical operators
def logical_operators_demo(a, b):
    # Using 'and' operator
    if a > 0 and b > 0:
        print(f"Both {a} and {b} are positive numbers.")
    else:
        print("At least one of the numbers is not positive.")

    # Using 'or' operator
    if a < 0 or b < 0:
        print("At least one of the numbers is negative.")
    else:
        print("Both numbers are non-negative.")

    # Using 'not' operator
    if not (a == 0):
        print(f"{a} is not zero.")
    else:
        print(f"{a} is zero.")

# Main block to test logical operators
if __name__ == "__main__":
    # User input
    a = int(input("Enter a value for a: "))
    b = int(input("Enter a value for b: "))
    
    logical_operators_demo(a, b)
