
def calculate_area(side_length):
    """
    Function to calculate area of square
    Parameter: side_length (float) - the length of one side
    Returns: area (float) - calculated area
    Formula: Area = side²
    """
    area = side_length ** 2
    return area

def calculate_perimeter(side_length):
    """
    Function to calculate perimeter of square
    Parameter: side_length (float) - the length of one side
    Returns: perimeter (float) - calculated perimeter
    Formula: Perimeter = 4 × side
    """
    perimeter = 4 * side_length
    return perimeter

# Main program execution starts here
print("=== Square Area and Perimeter Calculator ===")
print()

# Get side length from user input
# Using float() to handle decimal inputs
side = float(input("Enter the side length of the square: "))

# Call functions to calculate area and perimeter
# Functions return the calculated values
area = calculate_area(side)
perimeter = calculate_perimeter(side)

# Display results with clear formatting
print()
print("=== RESULTS ===")
print(f"Square with side length: {side}")
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
print()
print("Formulas used:")
print(f"Area = {side}² = {area}")
print(f"Perimeter = 4 × {side} = {perimeter}")