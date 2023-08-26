"""
@author : code8080.in
"""

# Interactive To-Do List in Python

# This is a single-line comment explaining the purpose of the program
print("Welcome to the Interactive To-Do List!")

# Variables to store the to-do list and user's choice
todo_list = []
choice = ""

# Using a while loop to keep the program running until the user decides to exit
while choice != "4":
    # Displaying the menu options
    print("\nMenu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")
    print("4. Exit")
    
    # Taking user input for their choice
    choice = input("Enter your choice (1/2/3/4): ")
    
    # Using if-elif-else to handle different choices
    if choice == "1":
        # Adding a task to the to-do list
        task = input("Enter the task you want to add: ")
        todo_list.append(task)
        print(f"'{task}' has been added to your to-do list.")
        
    elif choice == "2":
        # Displaying the tasks in the to-do list
        print("\nYour tasks:")
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")
            
    elif choice == "3":
        # Deleting a task from the to-do list
        task_num = int(input("Enter the task number you want to delete: "))
        if 0 < task_num <= len(todo_list):
            removed_task = todo_list.pop(task_num - 1)
            print(f"'{removed_task}' has been removed from your to-do list.")
        else:
            print("Invalid task number.")
            
    elif choice == "4":
        # Exiting the program
        print("Thank you for using the Interactive To-Do List. Goodbye!")
        
    else:
        # Handling invalid choices
        print("Invalid choice. Please choose a valid option from the menu.")

# This program demonstrates:
# - Basic Python syntax
# - Use of single-line comments
# - Variable declaration and usage
# - Conditional statements (if-elif-else)
# - Looping (while loop)
# - Taking user input
# - Displaying output
# - List manipulation (append, pop)
