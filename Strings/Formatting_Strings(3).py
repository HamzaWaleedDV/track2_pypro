"""
تنسيقات السلاسل النصية هي عملية اضافة متغيرات الي السلسلة النصية بأشكال مختلفة
"""

#Definition the two variable
name = 'Hamza'
age = 16

#Concatenate the string and variable with (+) or (,)
print('My name is ' + name)
print('My name is ', name)
print('=' * 9)
print('I am ' + str(age) + ' years old') #Note: the (str) is the method for convert any value passage to him to string
print('I am ', str(age) + ' years old')

#Concatenate the strings with %s for concatenate string, %f for concatenate the float number; you can add a point and a number between the % and f for choose numbers of Decimal Digits, %d for concatenate the digit number 
rank = 9.8

print("My name is %s. I am %d old years, my rank is %.1f." %(name, age, rank))

#Conctenate with format() method, It has three ways of definition

#First way
print('My name is {}, I am {} years old, My rank is {}.'.format(name, age, rank))
#ٍSecond way
print('My name is {1}, I am {2} years old, My rank is {0}.'.format(rank, name, age))
#Third way
print('My name is {name_key}, I am {age_key} years old, My rank is {rank_key}.'.format(rank_key = rank, name_key = name, age_key = age))

#Concatenate the strings with f_string
print(f'My name is {name}, I am {age} years old, My rank is {rank}.')