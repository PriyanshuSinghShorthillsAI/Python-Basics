a = [1, 2, 3]
b = a  # b refers to the same list object as a
c = a[:]  # c is a copy of the list a

print(a is b)  # True, because b refers to the same object as a
print(a is c)  # False, because c is a different object with the same content


a = [1, 2, 3]
b = a  # b refers to the same list object as a
c = a[:]  # c is a copy of the list a

print(a == b)  # True, because the values are the same
print(a == c)  # True, because the values are also the same
