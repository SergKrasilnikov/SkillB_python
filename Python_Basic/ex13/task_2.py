print('Задача 2. Функция максимума')

# Напишите программу,
# которая находит максимум из трёх чисел.
# Для этого используйте только функцию нахождения максимума из двух чисел.

def max_num(a, b):
    max_num = (a + b + abs(a - b)) / 2

    return max_num


while True:
    a = float(input('Введите первое число: '))
    b = float(input('Введите второе число: '))
    c = float(input('Введите третье число: '))

    ab_max = max_num(a, b)
    result = max_num(ab_max, c)

    print('Наибольшее число: ', result, '\n')

# ДОПОЛНИТЕЛЬНОЕ РЕШЕНИЕ
numbers = input('Введите числа через пробел: ')
print(max(numbers))