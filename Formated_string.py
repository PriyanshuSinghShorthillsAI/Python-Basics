name = "Priyanshu"
age = 23

# Using an f-string
greeting = f"My name is {name} and I am {age} years old."
print(greeting)  

# Using str.format()
name = "Priyanshu"
age = 23

greeting = "My name is {} and I am {} years old.".format(name, age)
print(greeting)  



name = "Priyanshu"
age = 23

greeting = "My name is %s and I am %d years old." % (name, age)
print(greeting)  


