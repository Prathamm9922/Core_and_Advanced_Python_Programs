
'''
# Python program to remove duplicate characters from a given string
'''

def remove_duplicates(string):
    seen = set()  # Set to track unique characters
    result = []  # List to store unique characters in order
    
    for char in string:
        if char not in seen or char == " ":  # Preserve spaces but remove duplicate letters
            seen.add(char)
            result.append(char)
    
    return "".join(result)

# Given input string
input_string = "String and String Function"

# Get result
output_string = remove_duplicates(input_string)

# Print output
print(output_string)

'''
output
String ad  Fuco

'''
