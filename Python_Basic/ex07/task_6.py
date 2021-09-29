print('Задача 6. Успеваемость в классе')

# В классе N человек.
# Каждый из них получил за урок по информатике оценку: 3, 4 или 5, двоек сегодня не было.
#
# Напишите программу,
# которая получает список оценок - N чисел - и выводит на экран сообщение о том,
# кого сегодня больше: отличников, хорошистов или троечников.

three = foure = five = 0
people = int(input('Человек в классе: '))
for points_list in range(0, people):
  point = int(input('Оценка: '))
  if point == 3:
    three += 1
  elif point == 4:
    foure += 1
  else:
    five += 1

if three > foure and three > five:
  print('Сегодня троечников больше.')
elif three < foure and foure > five:
  print('Сегодня хорошистов больше.')
elif three == foure and foure == five:
  print('Всех поровну.')
elif three == foure and foure > five:
  print('Троечников и хорошистов сегодня больше.')
elif three == five and foure < five:
  print('Троечников и отличников сегодня больше.')
elif foure == five and three < five:
  print('Хорошистов и отличников сегодня больше.')
else:
  print('Сегодня отличников больше.')