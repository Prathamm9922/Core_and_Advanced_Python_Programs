''' Python program to handle invalid integer input
'''
# Prompting the user for input
user_input = input("Enter an integer: ")

try:
    # Attempting to convert the input to an integer
    number = int(user_input)
    print("You entered a valid integer:", number)

# Handling invalid input that cannot be converted to an integer
except ValueError:
    print("Error: Invalid input. Please enter a valid integer.")

''' output

Enter an integer: 8
You entered a valid integer: 8

'''
