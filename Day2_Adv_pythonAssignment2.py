'''
2. You have a list of email addresses and you want to extract the domain part (the part after '@') from each email address. Example Data:

emails = [ "alice@example.com", "bob@sample.org", "charlie@mydomain.net" ]
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

# List of email addresses
emails = ["alice@example.com", "bob@sample.org", "charlie@mydomain.net"]

# Extract domain part from each email
domains = [email.split('@')[1] for email in emails]

# Print the extracted domains
print(domains)

'''
output

['JOHN DOE', 'EMILY JOHNSON']
['example.com', 'sample.org', 'mydomain.net']
'''
