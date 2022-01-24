# Homework 23.01.22
'''
# Task 1
try:
    name = input('Enter a name: ')
    surename = input('Enter a surename: ')
    print(name, surename, family_name)
except NameError:
    print('Нет отчества - допишите его')
    family_name = input('Family name: ')
    print(name, surename, family_name)

# Task 2
try:
    n1 = int(input('Enter num 1: '))
    n2 = int(input('Enter num 2: '))
    print(n1 + n2)
    print(n1 * n2)
    print(n1 - n2)
    print(n1 / n2)
except ZeroDivisionError:
    print('Ты делишь на 0')

try:
    do = ''
    while do != 'exit':
        do = input('Введите любое слово: ')
        num = int(input('Число: '))
        print(do + num)
except TypeError:
    print('Ты пытаешься сложить число и букву')
'''
def func():
    print('Hello! ')

def func2():
    a = 2
    b = 3
    print(a + b)

def func3():
    return 2 + 3 + 1

def func4(n1, n2, n3):
    print(n1 + n2 - n3)

def solution(string):
    print(string)
    print(string[::-1])

def checker(letter1, letter2):
    voc = 'abcABC'
    if letter1 not in voc or letter2 not in voc:
        return -1
    elif letter1.isupper() and letter2.isupper() or letter1.islower() and letter2.islower():
        return 1
    else:
        return 0

print(checker('A', 'A'))
print(checker('b', 'b'))
print(checker('A', 'c'))
print(checker('!!!!', 'C'))
