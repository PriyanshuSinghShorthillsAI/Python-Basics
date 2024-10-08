str1 = 'Hello'
str2 = "World"
str3 = '''This is a
multiline string'''
print(str1, str2)

greeting = "Hello" + " " + "World!"
print(greeting) 


repeat_str = "Hello" * 3
print(repeat_str)  


text = "Python"
print(text[0])  
print(text[-1])  # (negative index starts from the end)


slice_str = text[0:3] #(characters from index 0 to 2)
print(slice_str)


print(len("Hello")) 


print("Py" in "Python") 
print("Java" not in "Python")  


text = "Hello World"
print(text.upper())  
print(text.lower())  


text = "   Hello World   "
print(text.strip()) 


text = "I love Python"
new_text = text.replace("love", "like")
print(new_text)


text = "apple,banana,orange"
fruits = text.split(",") 
print(fruits)

new_text = "-".join(fruits)  
print(new_text)

text = "Hello, World!"
index = text.find("World")  # Output: 7
print(index)


print("Hello".isalpha())  
print("1234".isdigit())  
print("Hello123".isalnum()) 

"""
isalpha(), isdigit(), isalnum(): Check if the string contains only alphabets, digits, or alphanumeric characters.
"""

name = " Priyanshu  "
print(name.strip().upper()) 


