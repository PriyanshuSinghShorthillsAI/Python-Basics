# Built in Function and Methods

print("Hello, World!")  

name = "Priyanshu"
print(len(name)) 

num = 42
print(type(num))  

negative_num = -10
print(abs(negative_num)) 

numbers = [1, 2, 3, 4, 5]
print(sum(numbers))  


print(max(10, 20, 5))  

print(min(10, 20, 5)) 

numbers = [3, 1, 4, 2]
print(sorted(numbers))  

num = 3.14159
print(round(num, 2))  


user_input = input("Enter something: ")
print(f"You entered: {user_input}")



text = "hello"
print(text.upper())  

text = "apple,banana,orange"
fruits = text.split(",")
print(fruits)  


text = "I love Python"
print(text.replace("love", "like"))  # Output: I like Python


fruits = ["apple", "banana"]
fruits.append("orange")
print(fruits)  


fruits = ["apple", "banana", "orange"]
fruits.remove("banana")
print(fruits)  


numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)  


fruits = ["apple", "banana", "orange"]
fruit = fruits.pop()  # Removes 'orange'
print(fruit)  # Output: orange
print(fruits)  

person = {"name": "Priyanshu", "age": 24}
print(person.keys())  # dict_keys(['name', 'age'])

print(person.values())  # dict_values(['Priyanshu', 24])



fruits = ["apple", "banana", "orange"]

print(len(fruits))  
print(fruits[0].upper())  

fruits.append("mango")  
print(fruits)  











