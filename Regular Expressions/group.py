import re

phone = "415-555-1011"
search = re.search(r"(\d{3})-(\d{3}-\d{4})", phone)

print(search.group())
print(search.group(0))
print(search.group(1))
print(search.group(2))

print('-' * 30)

date = "27-05-2021"
split = re.search(r"(\d{2})-(\d{2})-(\d{4})", date)

day = split.group(1)
month = split.group(2)
year = split.group(3)

print(f'The day is: {day}, The month is: {month}, The year is: {year}')

day, month, year = split.groups()
print(f'The day is: {day}, The month is: {month}, The year is: {year}')