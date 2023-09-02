import re

#search()
txt = "My name is Hamza"

search = re.search("[A-Z]", txt)

print(search)
print(search.span())
print(search.group())


test = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office"
search = re.search(r"\d{3}-\d{3}-\d{4}", test)

print(search)
print(search.span())
print(search.group())

print('-' * 30)

#findall()
test1 = "Call me at 415-555-1011 tomorrow. 415-555-9999 is my office"
findall = re.findall(r"\d{3}-\d{3}-\d{4}", test1)

print(findall)

test_search = re.findall(r"A", test1)
print(test_search)

#Exam
# numbers = []

# print('Enter your number: ')
# number = input()

# def add_number_phone(num):

#     search = re.findall(r"\d{3}-\d{3}-\d{4}", num)

#     if search:
#         numbers.append(num)
#         print('Your number added successfully!!')
#     elif not search:
#         print('Your number added failed!!')

# add_number_phone(number)
# print(numbers)

print('-' * 30)

#sub()
string = """Hello my number is 415-555-1011 and
            my friends number is 658-984-2165"""

replace = re.sub(r"\d{3}-\d{3}-\d{4}", '415 555 1011', string, 1)
print(replace)

print('-' * 30)

txt = 'I am a student at Hsoub Academy'
replace = re.sub(r"Hsoub\sAcademy", 'Hsoub-Academy', txt)
print(replace)

#split()
txt = 'I am a student at Hsoub Academy'
search = re.split(r"\s", txt)
print(search)

search = re.split(r"\s", txt, 5)
print(search)

#Exam
txt = 'إستئناف-رفع-ملفات-جافاسكربت-بعد-قطع-الاتصال'

text = re.sub(r"-", " ", txt)
print(text)
#OR
test_r = 'إستئناف-رفع-ملفات-جافاسكربت-بعد-قطع-الاتصال'

split = re.split(r"-", test_r)
list2 = ' '.join(split)
print(list2)