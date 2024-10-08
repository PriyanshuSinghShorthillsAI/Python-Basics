# truthy_falsy_example.py

# Function to check truthy and falsy values
def check_truthy_falsy(value):
    if value:
        print(f"{value} is truthy.")
    else:
        print(f"{value} is falsy.")

# Main block to demonstrate truthy and falsy values
if __name__ == "__main__":
    # List of values to test
    values_to_test = [
        True,          # truthy
        False,         # falsy
        1,             # truthy (non-zero number)
        0,             # falsy
        "Hello",       # truthy (non-empty string)
        "",            # falsy (empty string)
        [1, 2, 3],     # truthy (non-empty list)
        [],            # falsy (empty list)
        None,          # falsy
        {},            # falsy (empty dictionary)
        {1: "one"},    # truthy (non-empty dictionary)
    ]

    # Check each value
    for val in values_to_test:
        check_truthy_falsy(val)

    # Demonstrate the use of truthy and falsy in a conditional
    print("\nDemonstrating truthy and falsy in a conditional:")
    user_input = input("Enter a number (0 or 1): ")
    if user_input:  # Non-empty string evaluates to truthy
        print(f"You entered a truthy value: {user_input}")
    else:           # Empty string evaluates to falsy
        print("You entered a falsy value (empty input).")
