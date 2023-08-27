"""
@author : code8080.in

In this interactive program, we'll create a simple calculator that performs basic arithmetic operations 
like addition, subtraction, multiplication, and division. The program will use a while loop to allow 
the user to perform multiple calculations without restarting the program.

# How to Use
    * Run the program.
    * Enter an arithmetic operator (+, -, *, /).
    * Enter the first and second numbers for the calculation.
    * The result will be displayed.
    * To exit the program, type exit.

# Key Points
    * The while True: loop allows for continuous calculations.
    * The perform_calculation function handles the arithmetic based on the operator.
    * The program checks for division by zero and handles it gracefully.
    * The program can be exited by typing exit.
"""

def perform_calculation(operator, num1, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Cannot divide by zero"
        return num1 / num2
    else:
        return "Invalid operator"

while True:
    print("\nSimple Calculator")
    print("Available operations: +, -, *, /")
    print("Type 'exit' to quit")

    operator = input("Enter an operator: ")
    if operator.lower() == 'exit':
        print("Exiting the calculator. Goodbye!")
        break

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    result = perform_calculation(operator, num1, num2)
    print(f"Result: {result}")
