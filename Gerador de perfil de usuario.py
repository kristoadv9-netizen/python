first_name = 'John'
last_name = 'Doe'

print(first_name, type(first_name))
print(last_name, type(last_name))

full_name = first_name + ' ' + last_name
print(full_name)

address = '123 Main Street'
address += ', Apartment 4B'
print(address)

is_student = True
print(is_student, type(is_student))

score = 80.5
print(score, type(score))

employee_age = 28

employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info)

experience_years = 5
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)

position = 'Data Analyst'
salary = 75000

employee_card = (
    f'Employee: {full_name} | '
    f'Age: {employee_age} | '
    f'Position: {position} | '
    f'Salary: ${salary}'
)
print(employee_card)

employee_code = 'DEV-2026-JD-001'

department = employee_code[0:3]
print(department)

year_code = employee_code[4:8]
initials = employee_code[9:11]

print(year_code)
print(initials)

last_three = employee_code[-3:]
print(last_three)