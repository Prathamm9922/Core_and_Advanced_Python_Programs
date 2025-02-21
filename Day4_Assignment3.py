# Function to check if a number is positive, negative, or zero
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Input: User enters a number
num = float(input("Enter a number: "))

# Check and print whether the number is positive, negative, or zero
result = check_number(num)
print(f"The number is {result}")

''' output
Enter a number: 66
The number is Positive
'''
