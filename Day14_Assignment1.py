''' Python program to handle ZeroDivisionError
'''
# Input: Two numbers from the user
numerator = float(input("Enter the numerator: "))
denominator = float(input("Enter the denominator: "))

try:
    # Attempting division
    result = numerator / denominator
    print("Result:", result)

# Handling division by zero error
except ZeroDivisionError:
    print("Error: Cannot divide by zero. Please enter a non-zero denominator.")


''' output

Enter the numerator: 5
Enter the denominator: 9
Result: 0.5555555555555556
'''
