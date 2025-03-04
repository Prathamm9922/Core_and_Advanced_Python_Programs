''' Function to read and display content from 'ABC.txt' line by line
'''
def read_file():
    try:
        # Open the file in read mode
        with open('ABC.txt', 'r') as file:
            # Read and display each line
            for line in file:
                print(line, end='')  # end='' prevents extra newline

    # Handle the case where the file does not exist
    except FileNotFoundError:
        print("Error: The file 'ABC.txt' was not found.")

# Call the function to read and display the file content
read_file()

'''
output

Error: The file 'ABC.txt' was not found.
'''
