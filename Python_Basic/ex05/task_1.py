print('Задача 1. Калькулятор опыта')
# Напишите программу,
# которая определяет уровень персонажа в компьютерной игре.
# Пользователь вводит число «очков опыта», а программа вычисляет уровень.
# Новый уровень даётся при достижении 1000, 2500 и 5000 «очков опыта».
# Начальный уровень равен 1.

# Пример:
# Введите количество опыта: 6000
# Ваш уровень: 4

# Пример 2:
# Введите количество опыта: 2000
# Ваш уровень: 2

exp = int(input('Введите количество опыта: '))
lvl = 1
if exp < 1000:
    pass
elif exp >= 1000 and exp < 2500:
    lvl = 2
elif exp >= 2500 and exp < 5000:
    lvl = 3
else:
    lvl = 4
print('Ваш уровень: ', lvl)