print('Задача 4. Урок информатики 3')

# На вход подаётся строка — это экспоненциальная форма числа.
# Напишите программу,
# которая выводит отдельно мантиссу и отдельно порядок этого числа.

# НОРМАЛЬНЫЙ ВАРИАНТ
string = input('Введите экспоненциальную форму числа: ')
power = mantissa = ''
flag = 1

for num_loop in string:
    if num_loop != 'e' and flag == True:
        mantissa += num_loop
    elif num_loop == 'e':
        flag = False
    else:
        power += num_loop

print('Мантисса равна:', mantissa)
print('Порядок равен:', power)

# ВАРИАНТ НЕ ОЧ

string = input('Введите экспоненциальную форму числа: ')
power = ''
mantissa = ''

for num_loop in string:
    if num_loop != 'e':
        mantissa += num_loop
    else:
        break

for num_loop2 in string[:: -1]:
    if num_loop2 != 'e':
        power += num_loop2
        power_res = power[:: -1]
    else:
        break

print('Мантисса равна:', mantissa)
print('Порядок равен:', power_res)