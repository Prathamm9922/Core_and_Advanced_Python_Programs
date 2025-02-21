'''
3. Finding the Factorial of a Given Number using a While Loop:
'''
# Input a number
num = int(input("Enter a number to find factorial: "))

# Initialize factorial as 1
fact = 1

# Loop to calculate factorial
while num > 0:
    fact = fact * num   # Multiply fact by current num
    num = num - 1       # Decrease num by 1

# Display the factorial
print("Factorial:", fact)

'''
output

Enter a number to find factorial: 9
Factorial: 362880

'''
