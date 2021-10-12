print('Задача 10. Яма ')


# В одной компьютерной текстовой игре рисуются всяческие элементы ландшафта.
#
# Напишите программу,
# которая получает на вход число N и выводит на экран числа в виде “ямы”:

# Введите число: 5
#
# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345

high = int(input('Глубина дыры: '))

for row in range(high):
  for col in range(high, high - row - 1, -1):
    print(col, end = '')
  print('.' * (high - row - 1) * 2, end = '')
  for col in range(high - row, high + 1, 1):
    print(col, end = '')
  print()