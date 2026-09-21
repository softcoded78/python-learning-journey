first_name = 'Icel'
last_name = 'Doe'
full_name = first_name + ' ' + last_name
address = '123 Main Street'
address += ', Apartment 4B'
employee_age = 19
employee_info = full_name + ' is ' + str(employee_age) + ' years old' + ' \nAddress:' + address
print(employee_info) # Icel Doe is 19 years old
print(address)
print(employee_age)

experience_years = 5
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info) # Experience: 5 years

position='Data Analyst'
salary=75000
employee_card=f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)

employee_code = 'DEV-2026-JD-001'
department = employee_code[0:3]
print(department) # DEV
year_code = employee_code[4:8]
print(year_code) # 2026
initials = employee_code[9:11]
print(initials) # JD
last_three=employee_code[-3:]
print(last_three) # 001


#Icel Doe is 19 years old
#Adress: 123 Main Street, Apartment 4B
#Experience: 5 years
#Employee: Icel Doe | Age: 19 | Position: Data Analyst | Salary: $75000
#DEV
#2026
#JD
#001
