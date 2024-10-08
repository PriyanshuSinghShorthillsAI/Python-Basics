# Example of break
for i in range(10):
    if i == 5:
        print("Breaking the loop at", i)
        break
    print(i)

# Example of continue
for i in range(10):
    if i % 2 == 0:
        continue  
    print(i)


# Example of return
def check_number(num):
    if num < 0:
        return "Negative number"
    return "Positive number"

result = check_number(-5)
print(result)  

