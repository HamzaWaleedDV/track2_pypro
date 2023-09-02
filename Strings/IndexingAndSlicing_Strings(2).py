"""
تقطيع السلاسل هو اقتطاع جزء من السلسلة النصية 
الفهرسة هو الوصول الي جزء معين من السلسلة النصية عن طريق رقمه
"""

#Defination the two strings
s1 = 'Hello Guys'
s2 = 'How are you?, I am fine Thank you'

#indexing the strings

print(s1[1])
print(s2[4])
#Note: The counting in Python Start from 0(zero)

#Slicing the strings \\\\ the syntax of the slicing is <name of the string>[start:end:step]
print(s1[0:6])
print(s2[3:8])

#If you do not enter any thing in strat, the slicing is start from the beginning of the string.
print(s1[:2])
#If you don't write anything at the end, the slicing will end at the end of the string.
print(s2[3:])
#The defualt value for steps is 1
print(s1[1:9])

#If you do not write anything at the end and the start, the slicing will print the all string
print(s2[:])

#The end number does not enter into slicing
print(s1[1:7:2])
print(s2[3:8:3])