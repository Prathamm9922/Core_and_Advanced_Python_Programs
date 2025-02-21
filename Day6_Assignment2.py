'''
2. Check Whether a Number is Palindrome or Not:
'''
# Input a number
num = int(input("Enter a number to check palindrome: "))

# Store the original number
original = num
rev = 0

# Loop to reverse the number
while num > 0:
    last_digit = num % 10          # Get last digit
    rev = (rev * 10) + last_digit  # Add digit to rev
    num = num // 10                # Remove last digit

# Check if original is same as reversed
if original == rev:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")

'''
output

Enter a number to check palindrome: 5
The number is a palindrome.
'''
