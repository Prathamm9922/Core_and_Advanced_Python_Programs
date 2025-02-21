# Function to find the largest number among three
def largest_of_three(a, b, c):
    # Compare all three numbers and return the largest one
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Input: User enters three numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find and print the largest number
largest = largest_of_three(num1, num2, num3)
print(f"The largest number is {largest}")

''' output
Enter the first number: 5
Enter the second number: 6
Enter the third number: 8
The largest number is 8.0
'''
