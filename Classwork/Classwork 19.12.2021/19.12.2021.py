'''
# Homework 19.12.2021
# Task 1 - Tuple editing

tup = (1,2,3)
tup[0] += 2

print(tup) # Error


# Task 2 - Animal counting
from random import randint

arr = []
res = 0

for elem in range(randint(2,10)):
    arr.append(bool(randint(0,1)))

print(arr)

for animal in arr:
    if animal == True:
        res += 1

print(f"Amount of animals: {res}")

# OR

print(f"Amount of animals: {arr.count(True)}")

# Task 3 - Tuple unique

tup = (1,2,2,3,3,4,5,5)
arr = []

for elem in tup:
    if elem not in arr:
        arr.append(elem)

print(f"Unique values: {arr}")

# Task 1 (New) - vowels and consonants

vowels = 'aeoui'
string = input('Enter a letter: ')

if string in vowels:
    print('Vowel')

else:
    print('Consonant')


# Task 2 (New) - Calculator

num_1, num_2 = int(input('Num 1: ')), int(input('Num 2: '))
math = input('Enter a math value (+, -, *, :): ')

if math == '+':
    print('Result: ', num_1 + num_2)

elif math == '-':
    print('Result: ', num_1 - num_2)

elif math == '*':
    print('Result: ', num_1 * num_2)

elif math == ':':
    print('Result: ', num_1 // num_2)

else:
    print('Error')

'''

# Classwork 19.21.2021
def add_1(value):
    print(value + 1)
    
num = int(input('Enter a number: '))

add_1(5)
add_1(num)
add_1(-3)

def add(num, num_2):
    print('Result: ', num + num_2)

def sub(num, num_2):
    print('Result: ', num - num_2)

def multi(num, num_2):
    print('Result: ', num * num_2)

def div(num, num_2):
    print('Result: ', num // num_2)

math = input('Element: ')
if math == '+':
    add(int(input()), int(input()))
elif math == '-':
    sub(int(input()), int(input()))
