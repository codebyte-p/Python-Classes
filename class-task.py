# Operators in Python

# Arithmetic Operators
a = 10
b = 5
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication  
print(a / b)  # Division
print(a % b)  # Modulus
print(a ** b)  # Exponentiation
print(a // b)  # Floor Division

# Comparison Operators
print(a > b)  # Greater than
print(a < b)  # Less than
print(a >= b)  # Greater than or equal to
print(a <= b)  # Less than or equal to
print(a == b)  # Equal to
print(a != b)  # Not equal to

# Logical Operators
p = True
q = False
print(p and q)  # Logical AND
print(p or q)  # Logical OR
print(not p)  # Logical NOT

# Assignment Operators
x = 5
print(x)  # Value Assign, Output: 5
x += 3
print(x)  # Add Assign, Output: 8
x -= 2
print(x)  # Subtract Assign, Output: 6
x *= 4
print(x)  # Multiply Assign, Output: 24
x /= 2
print(x)  # Divide Assign, Output: 12.0
x //= 3
print(x)  # Floor Divide Assign, Output: 4.0
x %= 3
print(x)  # Modulus Assign, Output: 1.0
x **= 2
print(x)  # Exponent Assign, Output: 1.0

# Bitwise Operators
m = 5  # Binary: 0101
n = 3  # Binary: 0011
print(m & n)  # Bitwise AND, Output: 1 (Binary: 0001)
print(m | n)  # Bitwise OR, Output: 7 (Binary: 0111)
print(m ^ n)  # Bitwise XOR, Output: 6 (Binary: 0110)
print(~m)  # Bitwise NOT, Output: -6 (Binary: 1010)
print(m << 1)  # Bitwise Left Shift, Output: 10 (Binary: 1010)
print(m >> 1)  # Bitwise Right Shift, Output: 2 (Binary: 0010)

# Membership and Identity Operators
print(3 in [1, 2, 3])  # Membership Operator, Output: True
print(4 not in [1, 2, 3])  # Membership Operator, Output: True
print(a is b)  # Identity Operator, Output: False
print(a is not b)  # Identity Operator, Output: True
print(a == b)  # Identity Operator, Output: True
print("py" in "Python")  # Membership Operator, Output: True

''' Operator Precedence
 The order of precedence determines the order in which operations are performed in an expression. Parentheses have the highest precedence, followed by exponentiation, 
 multiplication/division, addition/subtraction, and finally comparison and logical operators. '''