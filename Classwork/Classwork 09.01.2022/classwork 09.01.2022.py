'''
# print()
# input()

print(5)
print(2.5)
print('Hello world!')

print('Hello' * 3)
print('Hel' + 'lo')

# Example
# int() - Целые числа
# float() - Дробные числа
# str() - Строки
num = int(input('Введите число 1: '))
num2 = int(input('Введите число 2: '))
# +, -, *, /
print(num + num2)
print(num - num2)
print(num * num2)

print(num / num2)
print(num // num2)

print(5 == 5)
print(10 != 2)
print(4 >= 4)
print(4 > 4)
'''

num = int(input('Введите число 1: '))
num2 = int(input('Введите число 2: '))
operation = input('Что сделать с числами? ')

if operation == '+':
    print(num + num2)
elif operation == '-':
    print(num - num2)
elif operation == '*':
    print(num * num2)
elif operation == '**':
    print(num ** num2)
elif operation == '/':
    print(num / num2)
else:
    print('Подумай хорошенько :)')
    
