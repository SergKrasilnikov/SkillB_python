print('Задача 3. Число наоборот 2')


# Пользователь вводит два числа — N и K.
# Напишите программу,
# которая заменяет каждое число на число,
# которое получается из исходного записью его цифр в обратном порядке,
# затем складывает их,
# снова переворачивает и выводит ответ на экран.

# Пример:

# Введите первое число: 102
# Введите второе число: 123


# Первое число наоборот: 201
# Второе число наоборот: 321

# Сумма: 522
# Сумма наоборот: 225

def flip(num):
    results = 0
    while num > 0:
        index = num % 10
        num //= 10
        results *= 10
        results += index
    return results


a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))

num = a
a_flipped = flip(num)

num = b
b_flipped = flip(num)

sum_ab_flipped = a_flipped + b_flipped
sum_ab_fl_fl = flip(sum_ab_flipped)

print('\n\nПервое число наоборот:', a_flipped)
print('Второе число наоборот:', b_flipped, '\n')
print('Сумма:', sum_ab_flipped)
print('Сумма наоборот:', sum_ab_fl_fl)