print('Задача 9. ...Теперь можно посчитать и свою')

# Пользователь вводит 10 чисел.
# Напишите программу, которая проверяет, упорядочены ли они по возрастанию.
month_salary = index = 0
for salary_list in range(10):
  salary_input = int(input('Зарплата: '))
  if salary_input > month_salary:
    month_salary = salary_input
    index += 1
  else:
    print('Пора валить.')
    break
if index == 10:
  print('Все ок.')