def check_character_case(character):
    """
    Function to determine if character is uppercase or lowercase
    Parameter: character (str) - single character to check
    Returns: result (str) - 'uppercase', 'lowercase', or 'not a letter'
    
    Uses built-in string methods:
    - isupper(): checks if character is uppercase
    - islower(): checks if character is lowercase
    """
    if character.isupper():
        return "uppercase"
    elif character.islower():
        return "lowercase"
    else:
        return "not a letter"

# Main program execution starts here
print("=== Character Case Checker ===")
print()

# Get character input from user
char = input("Enter a single character: ")

# Validate input - check if user entered exactly one character
if len(char) == 1:
    # Call function to check the case of the character
    result = check_character_case(char)
    
    # Display the result
    print()
    print(f"Character entered: '{char}'")
    print(f"Result: The character '{char}' is {result}")
    
    # Additional information about the character
    if char.isalpha():  # Check if it's a letter
        print(f"'{char}' is a letter of the alphabet")
    else:
        print(f"'{char}' is not a letter (could be number, symbol, etc.)")
        
else:
    # Handle invalid input (more or less than 1 character)
    print()
    print("Error: Please enter exactly one character")
    print(f"You entered {len(char)} characters: '{char}'")