# Function to determine if a number is even or odd using the ternary operator
def is_even_or_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

# Main block to test the ternary operator
if __name__ == "__main__":
    number = int(input("Enter a number: "))
    result = is_even_or_odd(number)
    print(f"The number {number} is {result}.")
