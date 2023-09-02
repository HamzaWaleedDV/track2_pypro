import re


print('Enter your number: ')
number = input()

def is_phone(text):


    check = re.search(r"\d{3}-\d{3}-\d{4}", text)

    if check:
        print(f'the {text} is a valid phone number')
    else:
        print(f'the {text} is not a valid phone number')

is_phone(number)        