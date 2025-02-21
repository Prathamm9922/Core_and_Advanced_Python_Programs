# Full Python program to find the largest of two variables using ternary operator

# Declare two variables
a = int(input("Enter the value of variable a: "))
b = int(input("Enter the value of variable b: "))

# Using the ternary operator to determine the largest variable
largest = a if a > b else b

# Printing the largest value
print(f"The largest value between {a} and {b} is: {largest}")

 ''' output
 Enter the value of variable a: 15
Enter the value of variable b: 25
The largest value between 15 and 25 is: 25
'''
