#Dictionary = key value pairs aka Hashmaps

student = {'name': 'Rashmi', 'age':26, 'courses': ['Math', 'CompSci']}

# print(student['phone']) #Throws error
print(student.get('phone', '000')) #Returns None or the default value

student.update({'name':'Sam', 'age':27, 'phone':'555-888'})
# del student['age']

# name = student.pop('name')

# print(student.items())

for key, value in student.items():
    print(key, value)