''' # Python program to count letters, digits, and special symbols in a given string
'''
def count_elements(string):
    chars = digits = symbols = 0  # Initialize counters
    
    for char in string:
        if char.isalpha():  # Check if the character is a letter
            chars += 1
        elif char.isdigit():  # Check if the character is a digit
            digits += 1
        else:  # If it's neither a letter nor a digit, it is a special symbol
            symbols += 1
    
    return chars, digits, symbols

# Given input string
input_string = "P@#yn26at^&i5ve"

# Get counts
chars, digits, symbols = count_elements(input_string)

# Print output
print(f"Chars = {chars} Digits = {digits} Symbol = {symbols}")

''' output
Chars = 8 Digits = 3 Symbol = 4
'''
