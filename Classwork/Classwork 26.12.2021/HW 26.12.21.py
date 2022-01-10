# Tuple
# List => Ex: list(...) => [...]
'''
height = int(input('Введите ваш рост: '))
bmi = (height - 100) * 0.9

print(bmi)
'
# Sheeps dictionary

sheep_dict = {}
data = []
while True:
    data.append(input('Add name: '))
    data.append(input('Add age: ') + ' years')
    
    iden = int(input('Enter ID: '))

    if iden == 0:
        break
    
    sheep_dict[iden] = tuple(data)

    data = list(data)
    data.clear()
    print(data)
    
print(sheep_dict)
'
# Task 1 - Optimization

num = int(input('...'))

if num % 2 == 0:
    print('Odd')
    
else:
    print('Even')

# Task 2 - Mistake founding

w = input('Word: ')
s_word = input('Enter a searchable word: ')

print('Search word: ', w.count(s_word))

# Task 3 - Animal language

word = input('Enter a word: ')

if 'с' in word:
    word = word.replace("с", "ссс")
    
if 'С' in word:
    word = word.replace("С", "ССС")
print(word)


def add_1(n = 0):
    return n + 1

num = 5

m = add_1(num)
print(m)
'''

arr = [1,2,3,4,5,6,7,8,9,10]
counter = len(arr) - 1

while counter != 0 or arr != []:
    if arr[counter] % 5 == 0:
        print(arr[counter])
    else:
        print(f"{arr[counter]} не делится на 5")
    counter -= 1
    

