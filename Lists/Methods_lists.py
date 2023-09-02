'''
بعض الدوال التي يمكن استخدامها لعمل اشياء مختلفة علي القائمة
'''

# import a random madule
import random

employees = ['Hamdy', 'Hamza', 'Hasan', 'Reem']

#choice() دالة تقوم باختيار عنصر عشوائي من القائمة الممرره اليها
print(random.choice(employees))
print(random.choice(employees))
print(random.choice(employees))

#shuffle() دالة تقوم بإعادة ترتيب العناصر في القائمة بترتيب عشوائي
random.shuffle(employees)
print(employees)

print('-' * 30)

#append() تقوم بغضافة العناصر الممرره اليها الي نهاية القائمة
employees.append('yara')
print(employees)
print('-' * 30)

#insert() يقوم باضافة العناصر الممرره اليه الي القائمة في المكان الذي نحدده له
employees.insert(1, 'hosney')
print(employees)
print('-' * 30)

# OldEmployees = ['Osama', 'Alaa']
# employees.append(OldEmployees)
# print(employees)
print('-' * 30)

#extend()  تقوم باضافه قائمة الي قائمه اخري لكن بعد تفربغها فتضيفها كعناصر
OldEmployees = ['Osama', 'Alaa']
employees.extend(OldEmployees)
print(employees)
print('-' * 30)

#remove() يقوم بحذف العنصر الممرر اليه من القائمة الممرره اليه
#يطلق خطأ عند عدم وجود العنصر
employees.remove('Reem')
print(employees)
print('-' * 30)

# employees.remove('Anas') # Output: Error

employees = ['Hasan', 'Hadi', 'Hasan', 'Ahmed']
employees.remove('Hasan')
print(employees)
print('-' * 30)

#del statement يقوم بحذف العنصر الممرر اليه عبر القوسين المربعين []
del employees[0]
print(employees)
print('-' * 30)

#sort() يرتب عناصر القائمة تصاعديا حسب الاحرف الابجدية الانجليزية أو الارقام
#يمكننا عكس الترتيب اي جعله تنازليا بجعل قيمة reverse True   
numbers = [2, 5, 3.14, 1, -7]

numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

employees1 = ['Yara', 'Hamza', 'Ahmed', 'Reem']
employees1.sort()
print(employees1)
employees1.sort(reverse=True)
print(employees1)

"""
spam = [1, 3, 2, 4, 'Alice', 'Bob'] ====\
spam.sort() ============================ > #Error
print(spam) ============================/
"""

print('-' * 30)

#reverse() عكس عناصر القائمة 
names = ['Hamza', 'Hasan', 'Yara', 'Sara']
names.reverse()
print(names)
print('-' * 30)

#index() يعيد الموقع الخاص بعنصر ما
employees = ['Hasan', 'Hady', 'Yara', 'Ahmed', 'Hady']
print(employees.index('Hady'))
print('-' * 30)

#count() يرجع عدد تكرار العنصر الممرر اليه في القائمة
print(employees.count('Hady'))
print('-' * 30)

#copy() يصنع نسخة من القائمة
test = employees.copy()
print(test)

print('-' * 30)

#clear() يمسح جميع عناصر القائمة ويترك اقواسا فارغة
employees.clear()
print(employees)