print('Задача 2. Лестница')

# Пользователь вводит число N.
# Напишите программу, которая выводит такую “лесенку” из чисел:

# Введите число: 5
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

N = int(input('Введите число: '))

for row in range(1, N + 1):
  for col in range(1, N + 1):
    if col > row:
      print(' ', end = '\t')
    else:
      print(row, end = '\t')
  else:
    print(end = '\t')
  print('')