"""
توابع تساعد علي تنسيق وتعديل السلاسل النصية 
بما ان السلاسل النصية غير قابلة للتعديل 
فجميع تلك الدوال تقوم بأخذ نسخة من السلسلة النصية وعمل التغييرات عليها
فلاتؤثر علي السلسلة النصية الممررة اليها
"""

#Definition a variable
test = 'Hamza waleed, welcome'

#upper() تعيد السلسلة النصية بأحرف كبيره
print(test.upper())

print('-' * 30)

#lower() تعيد السلسلة النصية بأحرف صغيره
test1 = 'HAMZA WALEED, WELCOME'
print(test1.lower())

print('-' * 30)

#ولتغيير قيمة المتغير يجب تخزين القيمة العائدة من الدالة في نفس المتغير
test1 = test1.upper()
print(test1)

print('-' * 30)

# Example for knowing the importance of upper() and lower()
print('كيف حالك؟')
feelling = input()

if feelling.lower() == 'great':
    print('أنا أيضا أشعر بشعور عظيم')
else:
    print('أرجو أن يكون باقي يومك جيدا')

print('-' * 30)

#isupper() تتحقق مما اذا كانت السلسلة النصية بحروف كبيرة فاذا تحقق الشرط تعيد True والا تعيد False
test  = 'Hello, world!'
print(test.isupper())
print(test.upper().isupper())

print('-' * 30)

#islower() تتحقق مما اذا كانت السلسلة النصية بحروف صغيرة فاذا تحقق الشرط تعيد True والا تعيد False
print(test.islower())
print(test.lower().islower())

print('-' * 30)


#title() تجعل السلسلة عنوان بحيث تجعل اول حرف منها كبير أو الحرف الذي يكون بعد الرقم
test2 = 'hello 2nd'
print(test2.title())

print('-' * 30)

#capitalize() يجعل أول حرف في أول كلمة كبير والباقي كله صغير
txt = 'welcome to my 2nd World'
print(txt.capitalize())

print('-' * 30)

#swapcase() تقوم بتبديل الاحرف الصغيرة باحرف كبيرة والاحرف الكبيرة باحرف صغيرة
txt = 'Hello My Name Is Hamza'
print(txt.swapcase())

print('-' * 30)

#stratswith() تتحقق مما اذا كان النص المرر اليها موجود ببداية السلسلة النصية
txt = 'Hello, World'
print(txt.startswith('Hello'))#True
print(txt.startswith('world'))#False
#تستطيع البحث عن الاحرف
print(txt.startswith('H'))
#نستطيع اقتطاع جزء من السلسلة النصية والبحث به
print(txt.startswith('W', 7, 11))


print('-' * 30)

#endswith() تتحقق مما اذا كان النص المرر اليها موجود بنهاية السلسلة النصية
print(txt.endswith('World'))#True
print(txt.endswith('Hello'))#False
#تستطيع البحث عن الاحرف
print(txt.endswith('d'))
#نستطيع اقتطاع جزء من السلسلة النصية والبحث به
print(txt.endswith('o', 0, 5))

print('-' * 30)

# strip() يزيل جميع الفاراغات من يمين ويسار السلسلة النصية اذا لم نقم بتمرير اي قيمة
#اما لو مررنا قيمة ستحذف القيمة الممررة من يمين ويسار السلسلة النصية
s1 = '@@@Hello, world!@@@'
print(s1.strip())
print(s1.strip('@'))

print('-' * 30)

#lstrip() تحذف جميع الفراغات من يسار السلسلة النصية فقط اذا لم نقم بتمرير اي قيمة
#اما لو مررنا قيمة ستحذف القيمة الممررة من يسار السلسلة النصية
s2 = '@@@Hello, world!@@@'
print(s2.lstrip())
print(s2.lstrip('@'))

print('-' * 30)

#rstrip() تحذف جميع الفراغات من يمين السلسلة النصية فقط اذا لم ننقم بتمرير اي قيمة
#اما لو مررنا قيمة ستحذف القيمة الممررة من يمين السلسلة النصية
s3 = '@@@Hello, world!@@@'
print(s3.rstrip())
print(s3.rstrip('@'))

print('-' * 30)

#ويمكننا ايضا حذف اكتر من شيئ في نفس الوقت
test = '@#@#Hello, world@#@#'
print(test)
print(test.strip('@#'))
print(test.lstrip('@#'))
print(test.rstrip('@#'))

print('-' * 30)

#zfill() يقوم بإضافة صفر للسلسلة النصية
h = "1"
m = "9"
s = "5"

print(f'{h.zfill(2)}:{m.zfill(2)}:{s.zfill(2)}')

print('-' * 30)

#join() تعيد سلسلة نصية ناتجة عن ربط السلاسل النصية من كائن قابل للتكرار
list1 = ['Hello', 'world']
print(' '.join(list1))
print('-'.join(list1))
print('ABC'.join(list1))

print('-' * 30)

#split() يعيد قائمة عناصرها سلسلة نصية ويقسمها تبعا للفاصل الذي نمررة الية
ss1 = 'Hello world'
ss2 = 'Hello-world'
print(ss1.split(' '))
print(ss1.split('-'))

print('-' * 30)

#splitlines() يعيد قائمة عناصرها سلسلة نصية بحيث كل عنصر في القائمة هو سطر من السلسلة النصية
l1 = """hello
hamza
ahmed
Pyhton
C++
JS"""

l2 = "hello\nhamza\nahmed\nPyhton\nC++\nJS"

print(l1.splitlines())

print(l2.splitlines())

print('-' * 30)

#rjust() تقوم بإزاحة السلسلة النصية الي اليمين ljust() تقوم بإزاحة السلسلة النصية الي اليسار center() تقوم بإزاحة السلسلة النصية الي اليمين واليسار
word = 'Hello'

print(word.rjust(10))
print(word.rjust(10, '#'))

print('-' * 30)

print(word.ljust(10))
print(word.ljust(10, '#'))

print('-' * 30)

print(word.center(10))
print(word.center(11, '#'))

#expandtabs() نتحكم من خلالة في عدد المسافات التي يصنعها العامل \t
tabs = 'Hello\tWorld\twelcome'
print(tabs.expandtabs(10))

print('-' * 30)

#index() يبحث عن القيمة الممرره اليه ويعيد مكانها في السلسلة النصية
words = 'Hello World'

print(words.index('World'))
print(words.index('o'))

try:
    print(words.index('world', 0, 5))
except ValueError:
    print(-1)

#find() يعمل نفس عمل index لكنه ان لم يجد القيمة الممرره اليه يعيد -1
h = 'hello world'

print(h.find('World'))
print(h.find('o'))
print(h.find('world', 0, 5))

#repalce() يقوم بتبديل المعامل الاول مكان المعامل الثاني
text = "one plus one equal two"
print(text.replace("one", "1"))
print(text.replace("one", "1", 1))

print('---------------------------------------------------------------------------THE END---------------------------------------------------------------------------')