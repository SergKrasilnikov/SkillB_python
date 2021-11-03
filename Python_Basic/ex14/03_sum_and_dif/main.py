def summ(a):
    sum = 0
    for num_loop in str(a):
        sum += int(num_loop)
    return sum

def num_count(a):
    count = 0
    while a != 0:
        a //= 10
        count += 1
    return count

num = int(input('Введите число: '))

res_sum = summ(num)
res_count = num_count(num)

print('\n Сумма цифр:', res_sum, '\n Кол-во цифр в числе:', res_count, '\n Разность суммы и кол-ва цифр:', res_sum - res_count)

# зачёт!

