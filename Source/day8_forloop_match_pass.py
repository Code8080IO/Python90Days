"""
@author : code8080.in

In this program, the match statement is used to determine which formula to use for 
calculating the area based on the shape entered by the user. The pass statement is 
used in the default case (case _:) to do nothing when an 
unsupported shape is entered.
"""

def calculate_area(shape, dimensions):
    match shape:
        case "circle":
            radius = dimensions[0]
            area = 3.14159 * radius ** 2
            return f"The area of the circle is {area:.2f}"
        
        case "rectangle":
            length, width = dimensions
            area = length * width
            return f"The area of the rectangle is {area:.2f}"
        
        case "triangle":
            base, height = dimensions
            area = 0.5 * base * height
            return f"The area of the triangle is {area:.2f}"
        
        case _:
            pass  # Do nothing for unsupported shapes

    return "Unsupported shape"

# User input
shape = input("Enter the shape (circle, rectangle, triangle): ").lower()

if shape == "circle":
    radius = float(input("Enter the radius: "))
    dimensions = [radius]
elif shape == "rectangle":
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    dimensions = [length, width]
elif shape == "triangle":
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    dimensions = [base, height]
else:
    dimensions = []

# Calculate and display the area
result = calculate_area(shape, dimensions)
print(result)
