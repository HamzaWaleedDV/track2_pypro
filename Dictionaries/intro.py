'''
القواميس تتكون من مفاتيح كل مفتاح له قيمة ويمكن صنع قاموس عن طريق{}
لا يمكن تكرير مفتاح في نفس القاموس
'''

#Creat a dictionary
hadi = {
    'name': 'Hadi',
    'salary': 2000,
    'number': '7592022367683',
    'skills': ['HTML', 'CSS', "Bootstrab"]
}



print(hadi)
print(hadi['skills'])
print(hadi['number'])

print('-' * 30)

#dictionaries is not order 
list = ['cats', 'dogs', 'moose']
my_list = ['dogs','moose', 'cats']
print(my_list==list)

print('-' * 30)

dict = {'name': 'Hamza', 'age': 15, 'gender':'male'}
mydict = {'gender':'male', 'age': 15, 'name': 'Hamza'}

print(mydict == dict)

#example
birthday = {'hamza': 'April 1', 'sara': 'Dec 12', 'yara': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == '':
        break
    if name in birthday:
        print(f'The birthday for {name} is {birthday[name]}')

    else:
        print('The name is not found....')    
        print('What is thier birthday?')
        new_bday = input()
        birthday[name] = new_bday
        print('The name is added succssefully!!')

yara = {
    'frontEnd': {
        1:'HTML',
        2: 'CSS',
        3: 'Bootstrap'
    },
    'backEnd': {
        1: 'Django',
        2: 'Node.js',
        3: 'PHP'
    }
}

print(yara)
print(yara['frontEnd'])
print(yara['backEnd'])
print(yara['backEnd'][1])

print('---------------------------------------------------------------------------------THE END---------------------------------------------------------------------------------')
