print('Enter a sentence: ')
sentence = input()

list1 = sentence.split(' ')

list1.reverse()

result = ' '.join(list1)
print(result)