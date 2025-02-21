# Function to perform division of two numbers
def div(num1, num2):
    # Check if the denominator is not zero to avoid division by zero error
    if num2 != 0:
        result = num1 / num2  # Perform division
        print(f"The division of {num1} by {num2} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")

# Call the div() function with two numbers

div(10, 2)# Example: 10 divided by 2

''' output
The division of 10 by 2 is: 5.0
'''
