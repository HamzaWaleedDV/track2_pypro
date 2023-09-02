'''
دوال تساعدك علي التعامل مع القواميس
'''

#keys() تعيد قائمة فيها جميع مفاتيح القاموس
hadi = {
    'name': 'Hadi',
    'salary': 2000,
    'number': '7592022367683',
    'skills': ['HTML', 'CSS', "Bootstrab"]
}

print(hadi.keys())

#values() تعيد قائمة فيها جميع قيم القاموس

print(hadi.values())

#items() تعيد قائمة بها قيم القاموس علي هيئة مجموعه فيها قيمتان المفتاح وقيمته
print(hadi.items())

print('-' * 30)

#get()

hadi = {
    'name': 'Hadi',
    # 'salary': 2000,
    'number': '7592022367683',
    'skills': ['HTML', 'CSS', "Bootstrab"]
}

print(hadi['name'] + ' receive a salary of ' + str(hadi.get('salary', 'no salary')))

print('-' * 30)

#setdefault()
print(hadi)
print(hadi.setdefault('name', 'sara'))
print(hadi.setdefault('salary', 2000))
print(hadi)

if 'lang' not in hadi:
    hadi['lang'] = 'Python'
print(hadi)

print('-' * 30)

#update() 
numbers = {1: 'one', 2: 'three'}

print(numbers)
numbers.update({2: 'two'})
print(numbers)
numbers.update({3: 'Three'})
print(numbers)

print('-' * 30)

#clear()
numbers.clear()
print(numbers)

print('-' * 30)