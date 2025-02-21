'''
3. Find duplicate values from a list and display those:
'''
# List of numbers
numbers = [1, 2, 3, 2, 4, 5, 6, 4, 7, 8, 5]

# Empty list to store duplicates
duplicates = []

# Loop through each number by index
for i in range(len(numbers)):

    # Check if the number appears again later in the list
    if numbers[i] in numbers[i+1:] and numbers[i] not in duplicates:

        duplicates.append(numbers[i])  # Add to duplicates list if not already added

# Display the duplicate values
print("Duplicate values in the list:", duplicates)

''' output

Duplicate values in the list: [2, 4, 5]
'''
