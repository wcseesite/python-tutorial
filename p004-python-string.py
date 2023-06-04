# Creating a string
my_string = "Hello, World!"

# Accessing individual characters using indexing
print(my_string[0])  # Output: 'H'
print(my_string[-1])  # Output: '!'

# String formatting using the % operator
name = "John"
age = 30
print("My name is %s and I am %d years old" % (name, age))  # Output: My name is John and I am 30 years old

# String formatting using the format() method
name = "John"
age = 30
print("My name is {} and I am {} years old".format(name, age))  # Output: My name is John and I am 30 years old

# Commonly used string methods
my_string = "   Hello, World!   "
print(len(my_string))  # Output: 17
print(my_string.upper())  # Output: '   HELLO, WORLD!   '
print(my_string.strip())  # Output: 'Hello, World!'
print(my_string.replace('l', 'X'))  # Output: '   HeXXo, WorXd!   '
print(my_string.split(','))  # Output: ['   Hello', ' World!   ']
my_list = ['Hello', 'World!']
print(' '.join(my_list))  # Output: 'Hello World!'