# Arithmetic operators
x = 10
y = 5
print(x + y)  # Output: 15
print(x - y)  # Output: 5
print(x * y)  # Output: 50
print(x / y)  # Output: 2.0
print(x % y)  # Output: 0

# Comparison operators
x = 10
y = 5
print(x > y)  # Output: True
print(x < y)  # Output: False
print(x == y)  # Output: False
print(x != y)  # Output: True

# Logical operators
x = 10
y = 5
z = 7
print(x > y and x > z)  # Output: True
print(x > y or x < z)  # Output: True
print(not(x > y))  # Output: False

# Assignment operators
x = 10
y = 5
x += y  # Equivalent to x = x + y
print(x)  # Output: 15

# Bitwise operators
x = 10  # Binary representation: 1010
y = 5  # Binary representation: 0101
print(x & y)  # Output: 0 (binary representation: 0000)
print(x | y)  # Output: 15 (binary representation: 1111)

# Expressions
x = 10
y = 5
z = x + y * 2  # Expression
print(z)  # Output: 20

z = (x + y) * 2  # Expression with parentheses
print(z)  # Output: 30