# Homework 13.02.22
# Task 1 - Odd-Even number
def odd_even(number):
    if number % 2 == 0:
        print('Even') # Четное
    elif number % 2 == 1:
        print('Odd') # Нечетное

#odd_even(4)
#odd_even(7)
# Task 2 - Cycles
def cycle_data(radius):
    print(f"Площадь круга: {3.14 * radius ** 2}")
    print(f"Диаметр: {radius * 2}")
    print(f"Объем шара: {round(4/3 * 3.14 * radius ** 3, 2)}")

def fibonacci(fib, fib2, n):
    arr = [fib, fib2]
    for elem in range(n - 2):
        fib_sum = fib + fib2
        fib = fib2
        fib2 = fib_sum
        arr.append(fib_sum)
        print(arr)

fibonacci(1,1,10)
        
    
