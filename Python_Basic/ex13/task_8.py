print('Задача 8. Сумма ряда')

# Пользователь вводит действительное число
# "х" и точность "precision".

# P.S: Формулу смотреть на сайте :)


# Напишите программу,
# которая по число х вычисляет сумму ряда в точности до precision.


# Операцией возведения в степень и функцией factorial пользоваться нельзя.

# Пример:
# Введите точность: 0.001

# Введите x: 5
# Сумма ряда =  0.2836250150891709

def fucktorial(n):
  factorial = 1
  for i in range(2, n+1):
    factorial *= i

  return factorial

def power(a, b):
  results = 1
  for power_loop in range(b):
    results *= a

  return results

precision = float(input('Введите точность: '))
x = int(input('Введите x: '))

result = n = 0
S = 1

while abs(S) > precision:
  S = power(-1, n) * power(x, 2 * n) / fucktorial(2 * n)
  result += S
  n += 1

print('Сумма ряда =', result)