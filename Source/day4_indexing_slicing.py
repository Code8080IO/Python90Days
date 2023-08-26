"""
@author : code8080.in

Let's create a program that demonstrates 
Function to demonstrate string indexing and slicing
Function to demonstrate list indexing and slicing
Function to demonstrate tuple indexing and slicing
"""

# Function to demonstrate string indexing and slicing
def string_operations(user_string):
    print("\n--- String Operations ---")
    print(f"Original String: {user_string}")
    print(f"First Character: {user_string[0]}")
    print(f"Last Character: {user_string[-1]}")
    print(f"Slicing (first 5 characters): {user_string[:5]}")
    print(f"Slicing (last 5 characters): {user_string[-5:]}")
    print(f"Reverse String: {user_string[::-1]}")

# Function to demonstrate list indexing and slicing
def list_operations(user_list):
    print("\n--- List Operations ---")
    print(f"Original List: {user_list}")
    print(f"First Element: {user_list[0]}")
    print(f"Last Element: {user_list[-1]}")
    print(f"Slicing (first 3 elements): {user_list[:3]}")
    print(f"Slicing (last 3 elements): {user_list[-3:]}")
    print(f"Reverse List: {user_list[::-1]}")

# Function to demonstrate tuple indexing and slicing
def tuple_operations(user_tuple):
    print("\n--- Tuple Operations ---")
    print(f"Original Tuple: {user_tuple}")
    print(f"First Element: {user_tuple[0]}")
    print(f"Last Element: {user_tuple[-1]}")
    print(f"Slicing (first 3 elements): {user_tuple[:3]}")
    print(f"Slicing (last 3 elements): {user_tuple[-3:]}")
    print(f"Reverse Tuple: {user_tuple[::-1]}")

# Main Program
if __name__ == "__main__":
    # User Input for String
    user_string = input("Enter a string: ")
    string_operations(user_string)

    # User Input for List
    user_list = input("Enter a list separated by commas (e.g., 1,2,3): ").split(',')
    list_operations(user_list)

    # User Input for Tuple
    user_tuple_input = input("Enter a tuple separated by commas (e.g., 1,2,3): ")
    user_tuple = tuple(user_tuple_input.split(','))
    tuple_operations(user_tuple)
