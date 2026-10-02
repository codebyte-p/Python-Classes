# Assigning variables
name, age, address = (input("Enter your name: ")), int(input("Enter your age: ")), str(input("Enter your address: "))
# Using concatenation
print("My name is" + name + " and I am " + str(age) + " years old" + "Address is " + address) 
# Using f-string
print(f"My name is {name} and I am {age} years old and Address is {address}")
# Using % operator(OLD FORMAT)
print("MY name is %s and age is %d years old and Address is %s" % (name, age, address))
# Using format() method
print("My name is {0} and age is {1} years old and Address is {2}.".format(name, age, address))

# Single line comment
"""Multi-line comment (Shift + Alt + A)"""

num1 = input("Enter first number:")
num2 = input("Enter second number: ")
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))
sum = num1 + num2
print(f"Sum of {num1} and {num2} is {sum}")
sum2 = num3 + num4
print(f"Sum of {num3} and {num4} is {sum2}")