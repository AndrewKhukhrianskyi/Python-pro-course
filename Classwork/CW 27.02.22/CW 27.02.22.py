# Classwork 27.02.22
'''
from random import randint

def draw_head():
    return 'O'

def draw_body():
    return '|'

print('--------------')
print(r'|              /')
print(r'|              /')
print(f'|             {draw_head()}')
print(f'|              {draw_body()}')
print(f'|              {draw_body()}')
print('____________________')

print('Hello\nMy friend!')
'''

# https://www.codewars.com/kata/57a083a57cb1f31db7000028/train/python Задача доделать
def powers_of_two(n):
    mass = []
   
    for elem in range(0, n + 1):
        mass.append(2 ** elem)
    print(mass)

powers_of_two(2)
        