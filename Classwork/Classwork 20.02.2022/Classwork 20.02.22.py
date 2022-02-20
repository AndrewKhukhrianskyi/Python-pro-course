# +, -, *, /, //
# input()
#n1 = int(input('Ч1:  '))
#n2 = int(input('Ч2: '))
#print(n1 + n2)
# Homework 20.02.22
# Task 1 - Operator
'''
def operator(phone):
    if phone == '':
        print('Ошибка: Ничего не введено! ')
    
    kievstar = '067068097'
    mts = '066096'
    life = '063073'
    if phone[0:3] in kievstar:
        print('Номер киевстаровский!')
    elif phone[0:3] in mts:
        print('MTS')
    elif phone[0:3] in life:
        print('Life :)')
    else:
        print('Неизвестный оператор')

#operator(input('Number: '))
# Task 2 - Square sum
def square_sum(*numbers):
    list_num = list(numbers)
    for elem in range(len(list_num)):
        list_num[elem] **= 2
    print(list_num)
    print(sum(list_num))
square_sum(1,2,3)
'''

def add_data(*datas):
    return list(datas)

def filter_data(arr):
    filter_arr = []
    for elem in arr:
        if type(elem) is int:
            filter_arr.append(elem)
    return filter_arr

def odd_even(arr):
    odd_list = []
    even_list = []
    for elem in arr:
        if elem % 2 == 0:
            even_list.append(elem)
        else:
            odd_list.append(elem)
    return 'Сумма четн. ', sum(even_list),'Сумма нечетн.', sum(odd_list)
print(odd_even(filter_data(add_data('string', 11, 'even',
                                    25, 33, 40, 15, 'qqq'))))

