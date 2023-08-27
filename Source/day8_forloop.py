"""
@author : code8080.in

Here's an interactive Python program that lets the user explore for loops and the range function.
"""

print("Welcome to the For Loop and Range Function Explorer!")

choice = input("Do you want to see an example of a for loop? (yes/no): ")

if choice.lower() == 'yes':
    example_list = [1, 2, 3]
    print("Example List: ", example_list)
    print("Output:")
    for i in example_list:
        print(i)

choice = input("Do you want to see an example of the range function? (yes/no): ")

if choice.lower() == 'yes':
    print("Output:")
    for i in range(3):
        print(i)

