print('Задача 3. Это будет бомба')
# Программа спрашивает пользователя хочет ли он обезвредить бомбу сейчас.
#
# Если ответ “0” (то есть “нет”), то счетчик бомбы уменьшается.
# Если он достиг нуля, то программа выдаёт сообщение “Бомба взорвалась”,
# а если не достиг, то программа вновь переспрашивает,
# не хочет ли игрок обезвредить бомбу, и сообщает, сколько времени осталось до взрыва..
#
# Если ответ “да”, то программа выводит на экран сообщение о том,
# что бомба обезврежена и сколько секунд оставалось до взрыва.
# Используйте цикл for.

N_time = int(input('Кол-во секунд: '))
for discuss in range(N_time, -1, -1):
  if discuss == 0:
    print('Бомба взрывалась(')
    break
  print('До взрыва: ', discuss)
  responce = int(input('Не хочешь ли обезвредить бомбу? '))
  if responce != 0:
    print('Бомба обезврежена. До взрыва оставалось: ', discuss)
    break