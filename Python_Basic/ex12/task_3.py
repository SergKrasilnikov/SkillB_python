print('Задача 3. Апгрейд калькулятора')

# Напишите программу,
# которая спрашивает у пользователя число и действие,
# которое нужно с ним сделать:
# вывести сумму его цифр,
# вывести максимальную цифру или вывести минимальную цифру.
#
# Каждое действие оформите в виде отдельной функции,
# а основную программу зациклите.

def prog():
  while True:
    motion = int(input('\nДействие с числами:\n1 - сумма цифр числа;\n2 - максимальная цифра;\n3 - минимальная цифра.\n'))
    if motion < 1 or motion > 3:
      continue

    num = input('Введите число: ')
    if motion == 1:
      summ(num)
    elif motion == 2:
      maxi(num)
    elif motion == 3:
      mini(num)

def summ(num):
  results = 0
  for sum_loop in num:
    results += int(sum_loop)
  print(results)

def maxi(num):
  results = int(num[0])
  for max_loop in num:
    if int(max_loop) > results:
      results = int(max_loop)
  print(results)

def mini(num):
  results = int(num[0])
  for max_loop in num:
    if int(max_loop) < results:
      results = int(max_loop)
  print(results)

prog()