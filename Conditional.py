# conditional_logic_example.py

# Function to check if a number is positive, negative, or zero
def check_number(num):
    if num > 0:
        print(f"{num} is positive.")
    elif num < 0:
        print(f"{num} is negative.")
    else:
        print("The number is zero.")

# Function to categorize age
def categorize_age(age):
    if age < 13:
        return "Child"
    elif 13 <= age < 20:
        return "Teenager"
    elif 20 <= age < 65:
        return "Adult"
    else:
        return "Senior"

# Main block to test conditional logic
if __name__ == "__main__":
    # Check number
    number = float(input("Enter a number: "))
    check_number(number)

    # Check age category
    age = int(input("Enter your age: "))
    age_category = categorize_age(age)
    print(f"You are categorized as: {age_category}")

    # Demonstrating nested conditions
    score = int(input("Enter your exam score: "))
    if score >= 90:
        print("Grade: A")
    elif score >= 80:
        print("Grade: B")
    elif score >= 70:
        print("Grade: C")
    elif score >= 60:
        print("Grade: D")
    else:
        print("Grade: F")

    # Logical Operators
    a = True
    b = False
    if a and b:
        print("Both are True")
    elif a or b:
        print("At least one is True")
    else:
        print("Neither are True")

    # Using a switch-case-like structure with dictionary
    def switch_case(value):
        switcher = {
            1: "Option 1",
            2: "Option 2",
            3: "Option 3",
        }
        return switcher.get(value, "Invalid option")

    option = int(input("Choose an option (1-3): "))
    print(switch_case(option))
