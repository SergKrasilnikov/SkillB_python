print('Задача 6. Сумма факториалов')

# Напишите программу,
# которая запрашивает у пользователя число N
# и находит сумму факториалов 1! + 2! + 3! +... + N!

num = int(input('Конечное число: '))
factorial = 1
summ = 0

for num_list in range(1, num + 1):
    factorial *= num_list
    summ += factorial

print(summ)