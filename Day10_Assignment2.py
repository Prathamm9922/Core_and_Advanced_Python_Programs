'''
2. Get the largest and smallest number from a list (without built-in functions):
'''

# List of numbers
numbers = [23, 1, 45, 2, 67, 4, -5]

# Assume first element is both largest and smallest
largest = numbers[0]
smallest = numbers[0]

# Loop through each number in the list
for num in numbers:
    if num > largest:      # If current number is greater, update largest
        largest = num
        
    if num < smallest:     # If current number is smaller, update smallest
        smallest = num

# Display the largest and smallest numbers
print("Largest number in the list:", largest)
print("Smallest number in the list:", smallest)

''' output

Largest number in the list: 67
Smallest number in the list: -5

'''

