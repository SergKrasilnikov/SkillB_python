print('Задача 9. Пирамидка 2')


# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран,

# Пример:
#
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29

high = int(input('Высота пирамиды: '))
index = 1

for row in range(1, high + 1):
  print('\t' * (high - row), end = '')
  for col in range(1, row + 1):
    print(index, '\t\t', end = '')
    index += 2
  print()