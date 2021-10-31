print('Задача 5. Недоделка 2')

# вам нужно было написать код по следующим условиям:
# программа получает на вход два числа.
#
# В первом числе должно быть не меньше трёх цифр,
# во втором числе — не меньше четырёх,
# иначе программа выдаёт ошибку.
# Если всё нормально, то в каждом числе первая и последняя цифра меняются местами,
# а затем выводится их сумма.
#
#
# И тут вы натыкаетесь на программу,
# которая была написана прошлым программистом и которая как раз решает такую задачу!
# Однако старший программист сказал вам немного переписать этот код,
# чтобы он не выглядел так ужасно.
# Да и у вас самих от него вытекают глаза.
#
# Разбейте приведённую ниже программу на функции.
# Повторений кода должно быть как можно меньше.
# Также сделайте,
# чтобы в основной части программы был только ввод чисел, затем изменённые числа и вывод их суммы.

def count(temp):
    num_count = 0
    while temp > 0:
        num_count += 1
        temp = temp // 10

    return num_count


def flip(num, num_count):
    last_digit = num % 10
    first_digit = num // 10 ** (num_count - 1)
    between_digits = num % 10 ** (num_count - 1) // 10
    flipped = last_digit * 10 ** (num_count - 1) + between_digits * 10 + first_digit

    return flipped


while True:
    first_n = int(input("Введите первое число: "))
    first_num_count = count(first_n)
    if first_num_count < 3:
        print("\nВ первом числе меньше трех цифр.")
        continue

    second_n = int(input("\nВведите второе число: "))
    second_num_count = count(second_n)
    if second_num_count < 4:
        print("\nВо втором числе меньше четырёх цифр.")

    else:
        break

first_n = flip(first_n, first_num_count)
second_n = flip(second_n, second_num_count)

print('Изменённое первое число:', first_n)
print('Изменённое второе число:', second_n)
print('\nСумма чисел:', first_n + second_n)


# ВТОРОЕ РЕШЕНИЕ
def flip(num):
    last_digit = num % 10
    first_digit = num // 10 ** ((len(str(num))) - 1)
    between_digits = num % 10 ** ((len(str(num))) - 1) // 10
    first_n = last_digit * 10 ** ((len(str(num))) - 1) + between_digits * 10 + first_digit

    return first_n


def first_calc():
    first_n = input("Введите первое число: ")
    if len(first_n) < 3:
        print("В первом числе меньше трёх цифр.\n")
        exit()
    else:
        num = flip(int(first_n))
        print('Изменённое первое число:', num)
    return num


def second_calc():
    second_n = input("\nВведите второе число: ")
    if len(second_n) < 4:
        print("В первом числе меньше трёх цифр.\n")
        exit()
    else:
        num = flip(int(second_n))
        print('Изменённое второе число:', num)
    return num


first_res = first_calc()
second_res = second_calc()
print('\nСумма чисел:', first_res + second_res)