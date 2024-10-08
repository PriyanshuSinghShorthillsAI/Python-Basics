# iterables_example.py

def iterable_demo():
    # Example 1: List
    fruits = ["apple", "banana", "cherry"]
    print("Fruits List:")
    for fruit in fruits:
        print(fruit)

    # Example 2: Tuple
    colors = ("red", "green", "blue")
    print("\nColors Tuple:")
    for color in colors:
        print(color)

    # Example 3: Set
    unique_numbers = {1, 2, 3, 4, 5}
    print("\nUnique Numbers Set:")
    for number in unique_numbers:
        print(number)

    # Example 4: Dictionary
    person = {"name": "Alice", "age": 30, "city": "New York"}
    print("\nPerson Dictionary:")
    for key, value in person.items():
        print(f"{key}: {value}")

    # Example 5: String
    message = "Hello"
    print("\nString Characters:")
    for char in message:
        print(char)

if __name__ == "__main__":
    iterable_demo()
