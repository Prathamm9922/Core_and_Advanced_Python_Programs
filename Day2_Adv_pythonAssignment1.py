'''
1. You have a list of employee records, and you need to create a new list that contains the names of employees who work in the 'Sales' department, all in uppercase. Example Data:
'''


# List of employee records
employees = [ 
    {"name": "John Doe", "department": "Sales"}, 
    {"name": "Jane Smith", "department": "Marketing"}, 
    {"name": "Emily Johnson", "department": "Sales"}, 
    {"name": "Michael Brown", "department": "HR"} 
]

# Extract names of employees in 'Sales' department and convert to uppercase
sales_employees = [emp["name"].upper() for emp in employees if emp["department"] == "Sales"]

# Print the result
print(sales_employees)

'''
output
['JOHN DOE', 'EMILY JOHNSON']
'''
