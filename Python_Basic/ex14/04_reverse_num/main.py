import math

def flip(num):
    results = 0
    while num > 0:
        index = num % 10
        num //= 10
        results *= 10
        results += index
    return results

def int_to_str(a, b):
    results = str(a) + '.' + str(b)
    return results

def dividing(a):
    frac, integral = math.modf(a)
    return frac, integral

a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))

frac1, integral1 = dividing(a)
frac2, integral2 = dividing(b)

integral1_fl = flip(int(integral1))
frac1_fl = flip(int(round(frac1, 2) * 100))
integral2_fl = flip(int(integral2))
frac2_fl = flip(int(round(frac2, 2) * 100))

results1 = int_to_str(integral1_fl, frac1_fl)
results2 = int_to_str(integral2_fl, frac2_fl)

print('\nПервое число наоборот:', results1)
print('Второе число наоборот:', results2, '\n')
print('Сумма:', float(results1) + float(results2))