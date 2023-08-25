# This is a Python program to demonstrate Basic Syntax, Comments, and Variables

# Single-line Comment: The line above is a single-line comment.

'''
Multi-line Comment:
The lines enclosed between the triple quotes are often used as multi-line comments.
Although they are technically docstrings, they can be used for multi-line comments for simplicity.
'''

# Basic Syntax: Indentation and Statements
def greet(name):
    # The following line is indented to show the scope of the statement under the function.
    print("Hello, " + name + "!")  # This is a statement to print a greeting.

# Variables: Declaration and Assignment
greeting = "Welcome to Python programming!"  # A string variable
number = 10  # An integer variable
pi = 3.14  # A float variable

# Multiple Assignment
x, y, z = "Apple", "Banana", "Cherry"

# Output Variables
print(greeting)  # Outputs: Welcome to Python programming!
print("Value of number:", number)  # Outputs: Value of number: 10
print("Value of pi:", pi)  # Outputs: Value of pi: 3.14
print("Fruits:", x, y, z)  # Outputs: Fruits: Apple Banana Cherry

# Calling the function to demonstrate indentation
greet("Alice")  # Outputs: Hello, Alice!