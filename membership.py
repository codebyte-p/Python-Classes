# membership & identity
a = [1, 2, 3]
b = [1, 2, 3]

c = a


print(a is b)  # False, because a and b are different objects in memory
print(a is c)  # True, because c is a reference to the same object as a
print(a == b)  # True, because a and b have the same values
print(id(a))  # prints the memory address of a
print(id(b))  # prints the memory address of b
print(id(c))  # prints the memory address of c, which is the same as a