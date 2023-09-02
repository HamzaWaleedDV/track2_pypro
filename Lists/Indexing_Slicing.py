'''
الفهرسة في القوائم هي الوصول الي عنصر معين في القائمة عن طريق رقمه
التقطيع هو إقتطاع عدد معين من عناصر القائمة 
'''

#Indexing
employees = ['Hamdy', 'Hamza', 'Hasan', 'Reem']

print(employees)
print(employees[0])
print(employees[2])
print(employees[3])
print(employees[-1])
print(employees[-3])
# print(employees[50])

print('-' * 30)

#Slicing
print(employees[1:3])
print(employees[:3])
print(employees[1:])
print(employees[0:4:1])
print(employees[::1])
print(employees[0:4:2])
print(employees[::2])

print('-' * 30)

#Editing at list with Indexing
employees[0] = 'Sarah'
print(employees)
employees[-1] = 'yara'
print(employees)

employees[0:2] = 'hady', 'yomna'
print(employees)

#Clear list or part of list
'''
employees[0:2] = ''
employees[:] = ''
print(employees)
'''

print('-' * 30)

#for loop in lists
for employee in employees:
    print(employee)

#OR
for i in range(4):
    print(employees[i])    

#OR
for x in range(len(employees)):
    print(employees[x])

print('-' * 30)

for i in range(len(employees)):
    print(f'Index {i} in employee is: {employees[i]}')

print('=' * 30)

for number, name in enumerate(employees, 1):
    print(f'Index {number} in employee is: {name}')

print('-' * 30)

# in and not in
print('Hamza' not in employees)
print('yara' in employees)