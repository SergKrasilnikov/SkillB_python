print('Задача 7. Ход конём')


# В рамках разработки шахматного ИИ стоит новая задача.
# По заданным вещественным координатам коня
# и второй точки программа должна определить может ли конь ходить в эту точку.
#
# Используйте как можно меньше конструкций if и логических операторов.
# Обеспечьте контроль ввода.

# Введите местоположение коня:
# 0.071
# 0.118
# Введите местоположение точки на доске:
# 0.213
# 0.068
# Конь в клетке (0, 1). Точка в клетке (2, 0).
# Да, конь может ходить в эту точку.

import math

while True:
  print('Введите местоположение коня:')
  x1 = float(input())
  y1 = float(input())
  print('Введите местоположение точки на доске:')
  x2 = float(input())
  y2 = float(input())
  if x1 < 0 or x1 > 0.8 or x2 < 0 or x2 > 0.8 or y1 < 0 or y1 > 0.8 or y2 < 0 or y2 > 0.8:
    print('Введены неверные координаты.\n')
  else:
    break

pointX1 = math.floor(x1 * 10)
pointY1 = math.floor(y1 * 10)
pointX2 = math.floor(x2 * 10)
pointY2 = math.floor(y2 * 10)

print('Конь в клетке (' + str(pointX1) + ', ' + str(pointY1) + '). Точка в клетке (' + str(pointX2) + ', ' + str(pointY2) + ').')

x_move = pointX2 - pointX1
y_move = pointY2 - pointY1
if math.fabs(x_move) == 2 and math.fabs(y_move) == 1 or math.fabs(x_move) == 1 and math.fabs(y_move) == 2:
  print('Да, конь может ходить в эту точку.')
else:
  print('Конь не может ходить в эту точку.')