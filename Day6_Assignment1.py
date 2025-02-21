'''
1. Write a python program to reverse a number using a while loop. 
'''
# Input a number
num = int(input("Enter a number to reverse: "))

# Variable to store reversed number
rev = 0

# Loop to reverse the number
while num > 0:
    last_digit = num % 10          # Get last digit
    rev = (rev * 10) + last_digit  # Add digit to rev
    num = num // 10                # Remove last digit

# Display the reversed number
print("Reversed number:", rev)

''' output
Enter a number to reverse: 6
Reversed number: 6
'''
