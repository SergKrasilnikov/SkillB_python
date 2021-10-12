print('Задача 5. Простые числа')


#Напишите программу,
#которая считает количество простых чисел в заданной последовательности
#и выводит ответ на экран.


lower = int(input('Последовательность начало: '))
upper = int(input('Последовательность конец: '))
count = 0

for num_list in range (lower, upper+1):
 if num_list >= 1:
  for i in range (2, num_list):
   if num_list % i == 0:
    break
  else:
    count += 1
print ( "Количество простых чисел в диапазоне: ", count)
