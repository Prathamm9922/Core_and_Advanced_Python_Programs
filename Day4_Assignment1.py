# Function to check if a year is a leap year or not
def is_leap_year(year):
    # A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Input: User enters the year
year = int(input("Enter a year: "))

# Check and print whether the year is a leap year
if is_leap_year(year):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")


''' output
Enter a year: 2003
2003 is not a Leap Year
'''
