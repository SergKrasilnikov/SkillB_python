print('Задача 2. Долги')

# Сейчас операторам банка дали задание
# позвонить каждому пятому должнику из списка (они нумеруются с нуля) и спросить,
# сколько примерно денег каждый из них задолжал банку.
#
# Напишите программу,
# которая принимает на вход количество должников,
# затем спрашивает у каждого пятого (начиная с 0) его долг.
# В конце выводится общая сумма долгов.

# Пример:
#
# Введите количество должников: 13
# Должник с номером 0
# Сколько должны? 1000
# Должник с номером 5
# Сколько должны? 5000
# Должник с номером 10
# Сколько должны? 2000
# Общая сумма долга: 8000

num = int(input('Введите количество должников: '))
total_summ = index = 0
for amount in range(0, num, 5):
  print('Должник с номером ', amount)
  summ = int(input('Сколько должны? '))
  total_summ += summ
print('Общая сумма долга: ', total_summ)