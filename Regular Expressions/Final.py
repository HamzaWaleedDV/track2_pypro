import re

print('Enter your email: ')
email_i = input()

def check_email(email):

    checker = re.search(r'^[A-z0-9]+[_.-]?[A-z0-9]+@[a-z]+\.[a-z]+', email)

    if checker:
        print('Your email is correct!!')
    else:
        print('Your email is wrong!!')    

check_email(email_i)