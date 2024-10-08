# short_circuiting_example.py

# Function to demonstrate short-circuiting
def short_circuiting_example(a, b):
    # Using 'and' operator
    if a > 0 and (b / a > 1):
        print(f"Both conditions are true: {a} > 0 and {b} / {a} > 1")
    else:
        print("At least one condition is false.")

    # Using 'or' operator
    if a < 0 or (b / a > 1):
        print(f"At least one condition is true: {a} < 0 or {b} / {a} > 1")
    else:
        print("Both conditions are false.")

# Main block to test short-circuiting
if __name__ == "__main__":
    # Test cases
    a = int(input("Enter a value for a: "))
    b = int(input("Enter a value for b: "))
    short_circuiting_example(a, b)
