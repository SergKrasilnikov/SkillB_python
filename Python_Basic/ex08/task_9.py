print('Задача 9. Выражение')
#Дано число x.
#Напишите программу для вычисления следующего выражения

#( (x-1) * (x-3) * (x-7) * (x-15) * (x - 31) * (x-63))/
#( (x-2) * (x-4) * (x-8) * (x-16) * (x-32) * (x-64))

x = int(input('Число "x": '))

upper_results = results = 1
lower_index = 0

for results_list in range(1, 7):
  print('results: ', results_list)
  lower_index = 2 ** results_list
  results *= (x - (lower_index - 1)) / (x - lower_index)
print(results)