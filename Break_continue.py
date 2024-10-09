# example_loop_control.py

# Using break in a loop
print("Using break:")
for i in range(10):
    if i == 5:
        print("Breaking at 5")
        break  # Exit the loop when i is 5
    print(i)

# Using continue in a loop
print("\nUsing continue:")
for i in range(10):
    if i % 2 == 0:
        continue  # Skip the current iteration when i is even
    print(i)

# Using pass in a loop
print("\nUsing pass:")
for i in range(5):
    if i == 3:
        pass  # Placeholder, does nothing
    print(f"Number: {i}, pass did nothing for 3")
